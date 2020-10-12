#login to Azure and subscription
az login
az account list --output table #shows active and default subscriptions
az account set --subscription "Example" #replace Examle with subscription Name
az account show -o table #just to ensure current chosen subscription

# Create Resource Group - check possible locations using: az account list-locations -o table
az group create --name rg1 --location westeurope

# Create EventHub Namespace and Hub, name must be unique
az eventhubs namespace create --name SampleNamespaceName --resource-group rg1 -l westeurope
az eventhubs eventhub create --name SampleEventHubName --resource-group rg1 --namespace-name SampleNamespaceName

#say bye to Azure
az logout

<#
extras:
All Azure-cli commands https://docs.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest
 #>