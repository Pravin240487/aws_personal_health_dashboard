variable "environment" {
  default   = "testing"
  description = "Environment tag, e.g prod."
}

variable "AzureSMTP" {
  default   = "azuresmtp:credentials"
  description = "AZURE SMTP PASSWORD"
}

variable "sender" {
  default   = "personal_health_dashboard@amazon.com"
  description = "Sender's mail id"
}

variable "mail_receivers" {
  description = "Mail id's of the receivers to be updated here with comma seperation"
  default     = "individual_mailid@optum.com,distribution_list@ds.uhc.com"
  type        = string
}