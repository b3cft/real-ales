

## /brewery
### Method: GET
Return a list of breweries.

#### Arguments

Arguments are supplied as querystring parameters

* **count** (optional) 
 * default 20 
 * max 100

* **page** (optional)
 * default 1

* **sort** (optional)
 * default asc
 * asc or desc
   
#### Example response
    <breweries page="1" page="24" perpage="20" total="471">
      <brewery id="23">
        <name>...</name>
        <address>...</address>
        <postcode>...</postcode>
        <lat>...</lat>
        <long>...</long>
        ...
      </brewery>
    </breweries>

### Method: POST
Add a new brewery to the list

#### Arguments

Arguments as POST parameters

* **api_key** (required)
* **name** (required)
* **address** (optional)
* **postcode** (optional)
* **lat** (optional)
* **long** (optional)
* **website** (optional)
* **phone** (optional)
* **description** (optional)
* **api_sig** (required)

## /brewery/searchby/name/{name} (partial)
Method: **GET**

## /brewery/searchby/region/{region} 
Method: **GET**

## /brewery/searchby/postcode/{postcode} (nearest)
Method: **GET**

## /brewery/searchby/name/{name} (partial)
Method: **GET**

## /brewery/{id}
Method: **GET**

## /brewery/{id}/beer
Method: **GET,POST**

## /brewery/{id}/beer/{id} (canonical)
Method: **GET**

## /brewery/{id}/beer/{id}/recipe (canonical)
Method: **GET**

## /beer/{id}
Method: **GET**

## /beer/{id}/recipe
Method: **GET**

## /beer/by/name/{name} (partial)
Method: **GET**

## /beer/by/style/{style}
Method: **GET**

## /style/
Method: **GET,POST**

## /region/
Method: **GET,POST**

## /region/{region}
Method: **GET**
