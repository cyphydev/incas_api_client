# MessageEnrichment

This is the unified interface for message enrichment output.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrichment_type** | **str** | For discriminator | 
**message_uuid** | **str** |  | [optional] 
**provider_name** | **str** | The team (e.g., UIUC-DMG) who provides the enrichment. | [optional] 
**enrichment_name** | **str** | The enrichment (e.g., Concern-Stance) name for the enrichment. | [optional] 
**version** | **str** | The version within the same (provider, name). | [optional] 
**confidence** | **float** | The confidence that this enrichment is correct, expressed as a percentage between 0.0 and 1.0 | [optional] 
**attribute_value** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


