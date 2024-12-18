---
tags:
- 17/12/2024
---

# Creación de una aplicación de escritorio con Angular y Electron

Lo primero que debemos hacer es instalar [node.js][node] y tener un proyecto Angular preparado.

## Instalar Electron

```shell
npm install --save-dev electron@latest
```

## Configurar el proyecto

Creamos el archivo `main.js` en la raíz del proyecto:

```javascript
const {app, BrowserWindow} = require("electron");
const path = require('path');

let appWin;

createWindow = () => {
  appWin = new BrowserWindow({
    width: 800,
    height: 600,
    title: "AppName",
    resizable: false,
    webPreferences: {
      contextIsolation: false,
      nodeIntegration: true
    }
  });

  const indexPath = path.join(__dirname, 'dist', 'browser', 'index.html');

  appWin.loadURL(`file://${indexPath}`);

  appWin.setMenu(null);

  appWin.webContents.openDevTools();

  appWin.on("closed", () => {
    appWin = null;
  });
}

app.on("ready", createWindow);

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});
```

Debemos ir al archivo `package.json` y modificarlo:

```json
{
  "name": "app-name",
  "version": "0.0.0",
  "main": "main.js",
  "scripts": {
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
    "watch": "ng build --watch --configuration development",
    "test": "ng test",
    "electron": "ng build && electron",
    "dist": "electron-builder"
  }
}
```

Ahora debemos ir al archivo `angular.json` y modificar el `outputPath`:

```
"outputPath": "dist"
```

Por último debemos cambiar el `href` de `base` del archivo `index.html`:

```html

<base href="./">
```

## Arrancar el proyecto

```shell
npm run electron
```

## Comunicación entre Angular y Electron

- `ipcMain`: Se comunica de forma asíncrona desde el proceso principal a los procesos de renderizado. Es decir, desde el
  main.js al resto de la app.
- `ipcRenderer`: Se comunica de forma asíncrona desde un proceso de renderizado al proceso principal. Es decir, desde la
  app al main.js.

Lo primero que debemos hacer es crear un servicio de Angular que se encargue de manejar el `ipcRender` y que así podamos
usarlos desde toda la aplicación:

```typescript
import {Injectable} from "@angular/core";
import {IpcRenderer} from "electron";

@Injectable({
    providedIn: "root"
})
export class IpcService {
    private ipc: IpcRenderer;

    constructor() {
        if (window.require) {
            try {
                this.ipc = window.require("electron").ipcRenderer;
            } catch (e) {
                throw e;
            }
        } else {
            console.warn("Electron IPC was not loaded");
        }
    }

    public on(channel: string, listener: any): void {
        if (!this.ipc) {
            return;
        }
        this.ipc.on(channel, listener);
    }

    public once(channel: string, listener: any): void {
        if (!this.ipc) {
            return;
        }
        this.ipc.once(channel, listener);
    }

    public send(channel: string, ...args: any[]): void {
        if (!this.ipc) {
            return;
        }
        this.ipc.send(channel, ...args);
    }

    public removeAllListeners(channel: string): void {
        if (!this.ipc) {
            return;
        }
        this.ipc.removeAllListeners(channel);
    }
}
```

Ahora podemos llamar a estas funciones desde toda la App:

```typescript
import {Component, OnInit} from '@angular/core';
import {IpcService} from 'src/app/services/ipc.service';

@Component({
    selector: 'app-home',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
    pong: boolean = false;

    constructor(private ipcService: IpcService) {
    }

    ngOnInit(): void {
    }

    ping = (): void => {
        this.ipcService.send("message", "ping");
    }
}
```

Ahora volvemos al `main.js` para ver como recibimos el mensaje:

```javascript
const {app, ipcMain, BrowserWindow} = require("electron");

ipcMain.on("message", (event) => event.reply("reply", "pong"));
```

Esto hará que ipcMain escuche el canal “message” y que cuando llegue un mensaje, responder otro, que en este caso es
“pong”, por otro canal diferente llamado “reply”.

En nuestro componente de angular controlaremos la respuesta:

```typescript
import {Component, OnInit, ChangeDetectorRef, OnDestroy} from '@angular/core';
import {IpcService} from 'src/app/services/ipc.service';

@Component({
    selector: 'app-home',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit, OnDestroy {
    pong: boolean = false;

    constructor(private ipcService: IpcService, private cdRef: ChangeDetectorRef) {
    }

    ngOnInit(): void {
    }

    ping = (): void => {
        this.ipcService.send("message", "ping");
        this.ipcService.on("reply", (event: any, arg: string) => {
            this.pong = arg === "pong";
            this.cdRef.detectChanges();
        });
    }

    ngOnDestroy(): void {
        this.ipcService.removeAllListeners("reply");
    }
}
```

Al destruirse el componente nos aseguramos de borrar los listeners del canal, ya que pueden provocar fugas de memoria.

## Biblioteca electron-store

Esta biblioteca que permite de forma fácil trabajar con un almacenamiento local para Electron basado en clave-valor.

```shell
npm i electron-store
```

Ahora debemos crear un servicio para que se pueda usar fácilmente en toda la app:

```typescript
import { Injectable } from '@angular/core';
import * as ElectronStore from 'electron-store';

@Injectable({
  providedIn: 'root'
})
export class ElectronStoreService {
  private store: ElectronStore;
  constructor() {
    if (window.require) {
      try {
        const storeClass = window.require("electron-store");
        this.store = new storeClass();
      } catch (e) {
        throw e;
      }
    } else {
      console.warn("electron-store was not loaded");
    }
   }

   get = (key: string): any => {
    return this.store.get(key);
   }

   set = (key: string, value: any): void => {
     this.store.set(key, value);
   }
}
```

Ahora hay que añadir lo siguiente en el archivo `main.js`:

```javascript
const Store = require("electron-store");

const store = new Store();

if (!store.get("clicks")) {
    store.set("clicks", 0);
}
```

Ahora en cualquiera de nuestros componentes:

```typescript
import {Component, OnInit} from '@angular/core';
import {ElectronStoreService} from 'src/app/services/electron-store.service';

@Component({
    selector: 'app-game',
    templateUrl: './game.component.html',
    styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {
    clicks: number = 0;
    saved: boolean = true;

    constructor(private electronStoreService: ElectronStoreService) {
    }

    ngOnInit(): void {
        this.clicks = this.electronStoreService.get("clicks");
    }

    addClicks = (): void => {
        this.clicks++;
        this.saved = false;
    }

    save = (): void => {
        this.electronStoreService.set("clicks", this.clicks);
        this.saved = true;
    }
}
```

ngOnInit() se encarga de recuperar los clics guardados en local, addClicks() se llama cada vez que el botón es pulsado, y save() guarda la puntuación.

## Crear el instalador de la aplicación

### Asegurarse de haber construido la aplicación de angular previamente

```shell
ng build
```

### Crear el instalador

```shell
npm run dist
```

Se crea un archivo `.exe` en la carpeta `dist_electron`, que al ejecutarlo instala la app.

### Ejecutar la aplicación sin instalarla

```shell
npm run electron
```

[node]: ../../../others/node/index.md
