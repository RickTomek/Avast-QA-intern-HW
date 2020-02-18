Feature: Test Cart

      Scenario Outline: Test valid price 1 year
        Given I navigate to the Avast test page
        When I input "<count>" devices
        Then I am taken to cart page
        And I check final price

        Examples: numbers
          | count |
          | 1 |
          | 4 |
          | 5 |
          | 19 |
          | 20 |
          | 49 |
          | 50 |
          | 99 |
          | 100 |
          | 199 |
          | 200 |
          | 499 |
          | 500 |
          | 999 |

      Scenario Outline: Test 3 versions for 5 devices
        Given I navigate to the Avast test page
        When I click buy "<product>" "<price>"
        Then I am taken to cart page
        And I check final price

        Examples: buttons
          | product | price |
          | c-h-1  | $174.96|
          | c-h-2  | $224.96|
          | c-h-3  | $269.96|
          | bt-1   | $269.96|


