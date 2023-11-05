Feature: Product Management

  Scenario: Read a product by ID
    Given a product exists in the system
    When the user requests the product details by ID
    Then the system should return the product information

  Scenario: Update a product
    Given a product exists in the system
    When the user updates the product details
    Then the system should reflect the updated product information

  Scenario: Delete a product
    Given a product exists in the system
    When the user deletes the product
    Then the system should confirm the product is deleted

  Scenario: List all products
    Given multiple products exist in the system
    When the user requests to list all products
    Then the system should return a list of products

  Scenario: Search for a product by name
    Given a product with a known name exists in the system
    When the user searches for the product by name
    Then the system should return the correct product

  Scenario: Search for products by category
    Given products with specific categories exist in the system
    When the user searches for products by category
    Then the system should return products in the specified category

  Scenario: Search for products by availability
    Given products with various availabilities exist in the system
    When the user searches for products by availability
    Then the system should return products based on availability
