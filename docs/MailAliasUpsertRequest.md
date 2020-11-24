# MailAliasUpsertRequest

Mail alias upsert request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_if_exists** | **int** | Set to &#x60;1&#x60; when updating an alias. | 
**address** | **str** | Email format. | 
**forwards_to** | **str** | If adding a regular or catch-all alias, the format needs to be &#x60;user@example.com&#x60;. Multiple address can be separated by newlines or commas.  If adding a domain alias, the format needs to be &#x60;@example.com&#x60;.  | 
**permitted_senders** | **str** | Mail users that can send mail claiming to be from any address on the alias domain. Multiple address can be separated by newlines or commas.  Leave empty to allow any mail user listed in &#x60;forwards_to&#x60; to send mail claiming to be from any address on the alias domain.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


