# uiuc_incas_client.AdminApi

All URIs are relative to *https://incas.cs.illinois.edu:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_actor_post**](AdminApi.md#admin_actor_post) | **POST** /actor | 
[**admin_message_post**](AdminApi.md#admin_message_post) | **POST** /message | 

# **admin_actor_post**
> str admin_actor_post(body)



Add actors.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.AdminApi(uiuc_incas_client.ApiClient(configuration))
body = [uiuc_incas_client.UiucActor()] # list[UiucActor] | Array of actors

try:
    api_response = api_instance.admin_actor_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_actor_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[UiucActor]**](UiucActor.md)| Array of actors | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_message_post**
> str admin_message_post(body)



Add messages.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.AdminApi(uiuc_incas_client.ApiClient(configuration))
body = [uiuc_incas_client.UiucMessage()] # list[UiucMessage] | Array of messages

try:
    api_response = api_instance.admin_message_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_message_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[UiucMessage]**](UiucMessage.md)| Array of messages | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

