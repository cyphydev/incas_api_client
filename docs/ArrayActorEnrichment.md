# ArrayActorEnrichment

Defines a vector/matrix/tensor or multi-label enrichment for actor.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrichment_type** | **str** | For discriminator | 
**actor_uuid** | **str** |  | [optional] 
**provider_name** | **str** | The team (e.g., USC) who provides the enrichment. | [optional] 
**enrichment_name** | **str** | The enrichment (e.g., age, gender) name for the enrichment. | [optional] 
**version** | **str** | The version within the same (provider, enrichmentName). | [optional] 
**confidence** | **float** | The confidence that this enrichment is correct, expressed as a percentage between 0.0 and 1.0 | [optional] 
**attribute_value** | **[float]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


