Feature: Query student information

	As the teacher, I would like to query student information, so I can get their basic information and status 
	
	Scenario: Query student information by id
		Given I have following students in database
			|Id			|Name		|Gender		|Year of birth	|City		|
			|02043251	|Alex		|Male		|1988			|Beijing	|
			|02043252	|Keith		|Female		|1986			|Shanghai	|
			|02043253	|Jonathan	|Male		|1988			|Beijing	|
			|02043254	|Mike		|Male		|1988			|Heibei		|
			|02043255	|Lily		|Female		|1985			|Tianjin	|
		When I query student information by field name "Id" and value "02043251"
		Then I should get 1 records in the query result
		And I should see the result contains below records
			|Id			|Name		|Gender		|Year of birth	|City		|
			|02043251	|Alex		|Male		|1988			|Beijing	|