const localBackendOrigin = "http://localhost",
      localBackendPort = 4000;

export default (
    pathname: string,
    port: number = localBackendPort,
    origin: string = localBackendOrigin
):string => `${origin}${port && `:${port}`}${pathname}`;