# eDrilling Interview Assignment

## Prerequisite

You will be added to `329b0880-c06f-4382-a7d3-9e633d6d3fd9` Azure Active Directory application. (If your email is not already associated with Microsoft account, you will be prompted to create account.)

Test `JWT` can be obtained using Azure `az` CLI command (piping to `jq` utility is optional allowing to extract `accessToken` property from `JSON`):

```bash
az login --allow-no-subscriptions
az account get-access-token --resource 329b0880-c06f-4382-a7d3-9e633d6d3fd9 | jq -r .accessToken
```

## Task

1. Using any programming language and framework implement `HTTP` web server with the following endpoints:

    * `GET`: `/readTag`:

        This endpoint takes query parameter `name` (e.g. `/readTag?name=ConfigData.bit.totalFlowArea`), connects to `eDrillingHub` (see below), sends `read|$name` command over `WebSocket` as expects one of the following replies (string) from `WS` server:

        * `read|$name|...`: reply with `200` `HTTP` response with `JSON` (no need to parse reply from server):
  
            ```ts
            {
                response: string;
            }
            ```

        * `read_error|$name|...`: reply with `404` `HTTP` response

    * `POST`: `/writeTag`:

        This endpoint parses `JSON` body that needs to satisfy schema:

        ```ts
        {
            name: string; // required, e.g., ConfigData.bit.totalFlowArea
            value: number; // required, e.g. 0.5
        }
        ```

        Connect to `eDrillingHub` (see below) and send command:

        ```string
        write|$name|$unixTimestampMs|6|$value
        ```

        Reply with `200` `HTTP` response

    Both endpoints need to extract `JWT` from `HTTP` `Authorization` header (e.g., `Authorization: Bearer $TOKEN`) to pass it as `access_token` query parameter for `WebSocket` connection `URI`.

     To connect to `eDrillingHub`, connect to `WS` server: `wss://demo.edrilling.no/wells/3e927eeba131/app/ws?access_token=$TOKEN`

2. Add basic `OpenAPI v3.0.3` specification in `YAML` or `JSON` declaring query parameter schema for `GET` endpoint and `body` schema for `POST` endpoint.

3. Add `Dockerfile` and push resulting image to some public `Docker` registry so that container can be run and server tried out.
