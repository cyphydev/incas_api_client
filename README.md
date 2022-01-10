# uiuc-incas-client
This API document is defined based on INCAS Common Datatypes version 0.0.3.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import uiuc_incas_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import uiuc_incas_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorBatchGetBody() # ActorBatchGetBody | List of IDs and specifications

try:
    api_response = api_instance.actor_batch_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_batch_get: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | Type of entity to retrieve

try:
    api_response = api_instance.actor_count_get(entity_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_count_get: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.EnrichmentsBatchDeleteBody1() # EnrichmentsBatchDeleteBody1 | List of IDs and specifications

try:
    api_instance.actor_enrichments_batch_delete(body)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_delete: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.EnrichmentsBatchGetBody1() # EnrichmentsBatchGetBody1 | List of IDs and specifications

try:
    api_response = api_instance.actor_enrichments_batch_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_get: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, ActorEnrichment) | Map of IDs and enrichments

try:
    api_instance.actor_enrichments_batch_post(body)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_post: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, ActorEnrichment) | Map of IDs and enrichments

try:
    api_instance.actor_enrichments_batch_put(body)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_put: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
enrichment_name = 'enrichment_name_example' # str | 
provider_name = 'provider_name_example' # str | 
version = 'version_example' # str | 

try:
    api_instance.actor_enrichments_meta_delete(enrichment_name, provider_name, version)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_meta_delete: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.actor_enrichments_meta_get(enrichment_name=enrichment_name, provider_name=provider_name, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_meta_get: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorEnrichmentMeta() # ActorEnrichmentMeta | The new enrichment meta to add

try:
    api_instance.actor_enrichments_meta_post(body)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_meta_post: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorEnrichmentMeta() # ActorEnrichmentMeta | The new enrichment meta to update

try:
    api_instance.actor_enrichments_meta_put(body)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_meta_put: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Actor ID
enrichment_name = 'enrichment_name_example' # str | 
provider_name = 'provider_name_example' # str | 
version = 'version_example' # str | 

try:
    api_instance.actor_id_enrichments_delete(id, enrichment_name, provider_name, version)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_enrichments_delete: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Actor ID
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
dev = true # bool |  (optional)

try:
    api_response = api_instance.actor_id_enrichments_get(id, enrichment_name=enrichment_name, provider_name=provider_name, version=version, dev=dev)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_enrichments_get: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorEnrichment() # ActorEnrichment | The new enrichment to add
id = 'id_example' # str | Actor ID

try:
    api_instance.actor_id_enrichments_post(body, id)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_enrichments_post: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorEnrichment() # ActorEnrichment | The new enrichments to update
id = 'id_example' # str | Actor ID

try:
    api_instance.actor_id_enrichments_put(body, id)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_enrichments_put: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Actor ID
with_enrichment = true # bool | Whether to retrieve enrichments (optional)
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
dev = true # bool |  (optional)

try:
    api_response = api_instance.actor_id_get(id, with_enrichment=with_enrichment, enrichment_name=enrichment_name, provider_name=provider_name, version=version, dev=dev)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_get: %s\n" % e)

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
begin = 56 # int | Begin
end = 56 # int | End
entity_type = 'entity_type_example' # str | Type of entity to retrieve

try:
    api_response = api_instance.actor_list_get(begin, end, entity_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_list_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://incas.cs.illinois.edu:8443/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActorApi* | [**actor_batch_get**](docs/ActorApi.md#actor_batch_get) | **POST** /actor/batchGet | 
*ActorApi* | [**actor_count_get**](docs/ActorApi.md#actor_count_get) | **GET** /actor/count | 
*ActorApi* | [**actor_enrichments_batch_delete**](docs/ActorApi.md#actor_enrichments_batch_delete) | **POST** /actor/enrichments/batchDelete | 
*ActorApi* | [**actor_enrichments_batch_get**](docs/ActorApi.md#actor_enrichments_batch_get) | **POST** /actor/enrichments/batchGet | 
*ActorApi* | [**actor_enrichments_batch_post**](docs/ActorApi.md#actor_enrichments_batch_post) | **POST** /actor/enrichments/batch | 
*ActorApi* | [**actor_enrichments_batch_put**](docs/ActorApi.md#actor_enrichments_batch_put) | **PUT** /actor/enrichments/batch | 
*ActorApi* | [**actor_enrichments_meta_delete**](docs/ActorApi.md#actor_enrichments_meta_delete) | **DELETE** /actor/enrichments/meta | 
*ActorApi* | [**actor_enrichments_meta_get**](docs/ActorApi.md#actor_enrichments_meta_get) | **GET** /actor/enrichments/meta | 
*ActorApi* | [**actor_enrichments_meta_post**](docs/ActorApi.md#actor_enrichments_meta_post) | **POST** /actor/enrichments/meta | 
*ActorApi* | [**actor_enrichments_meta_put**](docs/ActorApi.md#actor_enrichments_meta_put) | **PUT** /actor/enrichments/meta | 
*ActorApi* | [**actor_id_enrichments_delete**](docs/ActorApi.md#actor_id_enrichments_delete) | **DELETE** /actor/{id}/enrichments | 
*ActorApi* | [**actor_id_enrichments_get**](docs/ActorApi.md#actor_id_enrichments_get) | **GET** /actor/{id}/enrichments | 
*ActorApi* | [**actor_id_enrichments_post**](docs/ActorApi.md#actor_id_enrichments_post) | **POST** /actor/{id}/enrichments | 
*ActorApi* | [**actor_id_enrichments_put**](docs/ActorApi.md#actor_id_enrichments_put) | **PUT** /actor/{id}/enrichments | 
*ActorApi* | [**actor_id_get**](docs/ActorApi.md#actor_id_get) | **GET** /actor/{id} | 
*ActorApi* | [**actor_list_get**](docs/ActorApi.md#actor_list_get) | **GET** /actor/list | 
*GraphApi* | [**actor_actor_graph_get**](docs/GraphApi.md#actor_actor_graph_get) | **GET** /actorActorGraph | 
*GraphApi* | [**actor_actor_graph_id_delete**](docs/GraphApi.md#actor_actor_graph_id_delete) | **DELETE** /actorActorGraph/{id} | 
*GraphApi* | [**actor_actor_graph_id_get**](docs/GraphApi.md#actor_actor_graph_id_get) | **GET** /actorActorGraph/{id} | 
*GraphApi* | [**actor_actor_graph_id_neighbor_get**](docs/GraphApi.md#actor_actor_graph_id_neighbor_get) | **GET** /actorActorGraph/{id}/neighbor | 
*GraphApi* | [**actor_actor_graph_id_put**](docs/GraphApi.md#actor_actor_graph_id_put) | **PUT** /actorActorGraph/{id} | 
*GraphApi* | [**actor_actor_graph_post**](docs/GraphApi.md#actor_actor_graph_post) | **POST** /actorActorGraph | 
*GraphApi* | [**actor_message_graph_get**](docs/GraphApi.md#actor_message_graph_get) | **GET** /actorMessageGraph | 
*GraphApi* | [**actor_message_graph_id_delete**](docs/GraphApi.md#actor_message_graph_id_delete) | **DELETE** /actorMessageGraph/{id} | 
*GraphApi* | [**actor_message_graph_id_get**](docs/GraphApi.md#actor_message_graph_id_get) | **GET** /actorMessageGraph/{id} | 
*GraphApi* | [**actor_message_graph_id_neighbor_get**](docs/GraphApi.md#actor_message_graph_id_neighbor_get) | **GET** /actorMessageGraph/{id}/neighbor | 
*GraphApi* | [**actor_message_graph_id_put**](docs/GraphApi.md#actor_message_graph_id_put) | **PUT** /actorMessageGraph/{id} | 
*GraphApi* | [**actor_message_graph_post**](docs/GraphApi.md#actor_message_graph_post) | **POST** /actorMessageGraph | 
*GraphApi* | [**message_message_graph_get**](docs/GraphApi.md#message_message_graph_get) | **GET** /messageMessageGraph | 
*GraphApi* | [**message_message_graph_id_delete**](docs/GraphApi.md#message_message_graph_id_delete) | **DELETE** /messageMessageGraph/{id} | 
*GraphApi* | [**message_message_graph_id_get**](docs/GraphApi.md#message_message_graph_id_get) | **GET** /messageMessageGraph/{id} | 
*GraphApi* | [**message_message_graph_id_neighbor_get**](docs/GraphApi.md#message_message_graph_id_neighbor_get) | **GET** /messageMessageGraph/{id}/neighbor | 
*GraphApi* | [**message_message_graph_id_put**](docs/GraphApi.md#message_message_graph_id_put) | **PUT** /messageMessageGraph/{id} | 
*GraphApi* | [**message_message_graph_post**](docs/GraphApi.md#message_message_graph_post) | **POST** /messageMessageGraph | 
*MessageApi* | [**message_batch_get**](docs/MessageApi.md#message_batch_get) | **POST** /message/batchGet | 
*MessageApi* | [**message_count_get**](docs/MessageApi.md#message_count_get) | **GET** /message/count | 
*MessageApi* | [**message_enrichments_batch_delete**](docs/MessageApi.md#message_enrichments_batch_delete) | **POST** /message/enrichments/batchDelete | 
*MessageApi* | [**message_enrichments_batch_get**](docs/MessageApi.md#message_enrichments_batch_get) | **POST** /message/enrichments/batchGet | 
*MessageApi* | [**message_enrichments_batch_post**](docs/MessageApi.md#message_enrichments_batch_post) | **POST** /message/enrichments/batch | 
*MessageApi* | [**message_enrichments_batch_put**](docs/MessageApi.md#message_enrichments_batch_put) | **PUT** /message/enrichments/batch | 
*MessageApi* | [**message_enrichments_meta_delete**](docs/MessageApi.md#message_enrichments_meta_delete) | **DELETE** /message/enrichments/meta | 
*MessageApi* | [**message_enrichments_meta_get**](docs/MessageApi.md#message_enrichments_meta_get) | **GET** /message/enrichments/meta | 
*MessageApi* | [**message_enrichments_meta_post**](docs/MessageApi.md#message_enrichments_meta_post) | **POST** /message/enrichments/meta | 
*MessageApi* | [**message_enrichments_meta_put**](docs/MessageApi.md#message_enrichments_meta_put) | **PUT** /message/enrichments/meta | 
*MessageApi* | [**message_id_enrichments_delete**](docs/MessageApi.md#message_id_enrichments_delete) | **DELETE** /message/{id}/enrichments | 
*MessageApi* | [**message_id_enrichments_get**](docs/MessageApi.md#message_id_enrichments_get) | **GET** /message/{id}/enrichments | 
*MessageApi* | [**message_id_enrichments_post**](docs/MessageApi.md#message_id_enrichments_post) | **POST** /message/{id}/enrichments | 
*MessageApi* | [**message_id_enrichments_put**](docs/MessageApi.md#message_id_enrichments_put) | **PUT** /message/{id}/enrichments | 
*MessageApi* | [**message_id_get**](docs/MessageApi.md#message_id_get) | **GET** /message/{id} | 
*MessageApi* | [**message_list_get**](docs/MessageApi.md#message_list_get) | **GET** /message/list | 

## Documentation For Models

 - [Actor](docs/Actor.md)
 - [ActorActorGraph](docs/ActorActorGraph.md)
 - [ActorActorGraphDB](docs/ActorActorGraphDB.md)
 - [ActorBatchGetBody](docs/ActorBatchGetBody.md)
 - [ActorEnrichment](docs/ActorEnrichment.md)
 - [ActorEnrichmentMeta](docs/ActorEnrichmentMeta.md)
 - [ActorMessageEdge](docs/ActorMessageEdge.md)
 - [ActorMessageGraph](docs/ActorMessageGraph.md)
 - [ActorMessageGraphDB](docs/ActorMessageGraphDB.md)
 - [ActorToActorEdge](docs/ActorToActorEdge.md)
 - [ActorToMessageEdge](docs/ActorToMessageEdge.md)
 - [Annotation](docs/Annotation.md)
 - [ArrayActorEnrichment](docs/ArrayActorEnrichment.md)
 - [ArrayActorEnrichmentMeta](docs/ArrayActorEnrichmentMeta.md)
 - [ArrayMessageEnrichment](docs/ArrayMessageEnrichment.md)
 - [ArrayMessageEnrichmentMeta](docs/ArrayMessageEnrichmentMeta.md)
 - [BaseActorEnrichment](docs/BaseActorEnrichment.md)
 - [BaseActorEnrichmentMeta](docs/BaseActorEnrichmentMeta.md)
 - [BaseEdge](docs/BaseEdge.md)
 - [BaseGraph](docs/BaseGraph.md)
 - [BaseMessageEnrichment](docs/BaseMessageEnrichment.md)
 - [BaseMessageEnrichmentMeta](docs/BaseMessageEnrichmentMeta.md)
 - [CategoryActorEnrichment](docs/CategoryActorEnrichment.md)
 - [CategoryActorEnrichmentMeta](docs/CategoryActorEnrichmentMeta.md)
 - [CategoryMessageEnrichment](docs/CategoryMessageEnrichment.md)
 - [CategoryMessageEnrichmentMeta](docs/CategoryMessageEnrichmentMeta.md)
 - [EnrichmentsBatchDeleteBody](docs/EnrichmentsBatchDeleteBody.md)
 - [EnrichmentsBatchDeleteBody1](docs/EnrichmentsBatchDeleteBody1.md)
 - [EnrichmentsBatchGetBody](docs/EnrichmentsBatchGetBody.md)
 - [EnrichmentsBatchGetBody1](docs/EnrichmentsBatchGetBody1.md)
 - [ExtraAttribute](docs/ExtraAttribute.md)
 - [ExtraAttributes](docs/ExtraAttributes.md)
 - [GeoLocation](docs/GeoLocation.md)
 - [Links](docs/Links.md)
 - [MediaResource](docs/MediaResource.md)
 - [Message](docs/Message.md)
 - [MessageBatchGetBody](docs/MessageBatchGetBody.md)
 - [MessageEnrichment](docs/MessageEnrichment.md)
 - [MessageEnrichmentMeta](docs/MessageEnrichmentMeta.md)
 - [MessageMessageGraph](docs/MessageMessageGraph.md)
 - [MessageMessageGraphDB](docs/MessageMessageGraphDB.md)
 - [MessageToActorEdge](docs/MessageToActorEdge.md)
 - [MessageToMessageEdge](docs/MessageToMessageEdge.md)
 - [NumericalActorEnrichment](docs/NumericalActorEnrichment.md)
 - [NumericalActorEnrichmentMeta](docs/NumericalActorEnrichmentMeta.md)
 - [NumericalMessageEnrichment](docs/NumericalMessageEnrichment.md)
 - [NumericalMessageEnrichmentMeta](docs/NumericalMessageEnrichmentMeta.md)
 - [Offset](docs/Offset.md)
 - [OneOfActorEnrichment](docs/OneOfActorEnrichment.md)
 - [OneOfActorEnrichmentMeta](docs/OneOfActorEnrichmentMeta.md)
 - [OneOfActorMessageEdge](docs/OneOfActorMessageEdge.md)
 - [OneOfMediaTypeAttributes](docs/OneOfMediaTypeAttributes.md)
 - [OneOfMessageEnrichment](docs/OneOfMessageEnrichment.md)
 - [OneOfMessageEnrichmentMeta](docs/OneOfMessageEnrichmentMeta.md)
 - [RedditData](docs/RedditData.md)
 - [Response](docs/Response.md)
 - [TextActorEnrichment](docs/TextActorEnrichment.md)
 - [TextActorEnrichmentMeta](docs/TextActorEnrichmentMeta.md)
 - [TextMessageEnrichment](docs/TextMessageEnrichment.md)
 - [TextMessageEnrichmentMeta](docs/TextMessageEnrichmentMeta.md)
 - [TwitterData](docs/TwitterData.md)
 - [UiucActor](docs/UiucActor.md)
 - [UiucActorDB](docs/UiucActorDB.md)
 - [UiucMessage](docs/UiucMessage.md)
 - [UiucMessageDB](docs/UiucMessageDB.md)
 - [UiucSegment](docs/UiucSegment.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


