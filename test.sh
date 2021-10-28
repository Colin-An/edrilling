#!/bin/bash

set -e

TOKEN=$(az account get-access-token --resource 329b0880-c06f-4382-a7d3-9e633d6d3fd9 -t 843c50bf-97b6-4efe-a805-2108a2e76a71 | jq -r .accessToken)

HOST=localhost:8081

http --follow $HOST/api/v1/service/getServiceInfo

http --follow POST $HOST/api/v1/service/TestTask data==abc

http $HOST/api/v1/tag/readTag

http $HOST/api/v1/tag/readTag name==abc

http $HOST/api/v1/tag/readTag name==abc "Authorization: Bearer $TOKEN"

http $HOST/api/v1/tag/readTag name==abc "access-token: Bearer $TOKEN"

http $HOST/api/v1/tag/readTag name==ConfigData.bit.totalFlowArea "access-token: Bearer $TOKEN"

http $HOST/api/v1/tag/readTag name==ConfigData.bit.totalFlowArea "access-token: Bearer $TOKEN 1"

http POST $HOST/api/v1/tag/readTag name==ConfigData.bit.totalFlowArea "access-token: Bearer $TOKEN"

http POST $HOST/api/v1/tag/writeTag name==ConfigData.bit.totalFlowArea "access-token: Bearer $TOKEN"

RANDOM_VALUE=$RANDOM
echo Random value $RANDOM_VALUE

http $HOST/api/v1/tag/writeTag name=ConfigData.bit.totalFlowArea value=$RANDOM_VALUE "access-token: Bearer $TOKEN"

http $HOST/api/v1/tag/readTag name==ConfigData.bit.totalFlowArea "access-token: Bearer $TOKEN"

http $HOST/api/v1/tag/writeTag name=ConfigData.bit.totalFlowArea value=abc "access-token: Bearer $TOKEN"

http $HOST/api/v1/tag/writeTag "access-token: Bearer $TOKEN" < test0.json

http $HOST/api/v1/tag/writeTag "access-token: Bearer $TOKEN" < test1.json

http $HOST/api/v1/tag/writeTag "access-token: Bearer $TOKEN" < test2.json
