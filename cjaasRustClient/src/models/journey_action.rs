/*
 * Azure Functions OpenAPI Extension
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct JourneyAction {
    /// Name
    #[serde(rename = "name", skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,
    /// Organization
    #[serde(rename = "organization", skip_serializing_if = "Option::is_none")]
    pub organization: Option<String>,
    /// Namespace
    #[serde(rename = "namespace", skip_serializing_if = "Option::is_none")]
    pub namespace: Option<String>,
    /// Version
    #[serde(rename = "version", skip_serializing_if = "Option::is_none")]
    pub version: Option<String>,
    /// Active
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<bool>,
    /// Template Id
    #[serde(rename = "templateId", skip_serializing_if = "Option::is_none")]
    pub template_id: Option<String>,
    /// Rules
    #[serde(rename = "rules", skip_serializing_if = "Option::is_none")]
    pub rules: Option<serde_json::Value>,
    /// List of actions
    #[serde(rename = "actions", skip_serializing_if = "Option::is_none")]
    pub actions: Option<Vec<crate::models::Action>>,
}

impl JourneyAction {
    pub fn new() -> JourneyAction {
        JourneyAction {
            name: None,
            organization: None,
            namespace: None,
            version: None,
            active: None,
            template_id: None,
            rules: None,
            actions: None,
        }
    }
}


