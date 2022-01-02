# MessageMessageGraph

Defines the message-to-message graph.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph_id** | **str** | This is the unique ID associated to the graph instance. | [optional] 
**provider_name** | **str** | The team who builds this graph. | [optional] 
**graph_name** | **str** | The name assigned to the algorithm/method used to construct the graph. | [optional] 
**distance_name** | **str** | The distance function used to build the graph. | [optional] 
**version** | **str** | The version ID within the same (providerName, graphName, distanceName) | [optional] 
**time_stamp** | **str** | Used for distinguishing the dynamic graph on time dimension. | [optional] 
**platform** | **str** |  | [optional] 
**enrichment_name** | **str** | The type of enrichment used to construct the msg2msg graph. | [optional] 
**edges** | [**[MessageToMessageEdge]**](MessageToMessageEdge.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


