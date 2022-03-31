terraform {

  required_version = ">=0.12"
  
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.0.2"
    }
  }
}

provider "azurerm" {
    features {}
}

resource "azurerm_storage_account" "test_sa" {
  name                     = "synsast12345"
  resource_group_name      = "Synechron-CH-RG"
  location                 = "Central US"
  account_tier             = "Standard"
  account_replication_type = "GRS"
}