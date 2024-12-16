# Servicios

Para crear un servicio usaremos el comando:

```shell
ng generate service directorio/servicio
```

## Comunicación con una API

Debemos importar e inyectar `HttpClient` en nuestro servicio:

```typescript
import { HttpClient } from '@angular/common/http';

constructor(private httpClient: HttpClient) {}
```

### Comunicación con cabeceras

```typescript
getInformation() {
    let request_headers = new HttpHeaders({headers1: "header1"});
    return this.httpClient.get<any>(API_URL, {headers: request_headers});
}
```

### Comunicación con cuerpo

```typescript
getInformation(body) {
    return this.httpClient.post<any>(API_URL, body);
}
```

### GET

```typescript
getInformation() {
    return this.httpClient.get<any>(API_URL)
}
```

### PUT

```typescript
getInformation(body) {
    return this.httpClient.put<any>(API_URL, body)
}
```

### POST

```typescript
getInformation() {
    return this.httpClient.post<any>(API_URL, body)
}
```

### DELETE

```typescript
getInformation() {
    return this.httpClient.get<any>(API_URL)
}
```

### Llamar al servicio desde un componente

```typescript
constructor(private api_service: ServiceName) {}
info = []
this.api_service.getInformation().subscribe((response) => {this.info = response});
```

