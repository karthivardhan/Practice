
Feature: Verify Books are added and Deleted using API

	Scenario: Verify add book via API

		Given the book details which needs to be added to Library
		When we execute add book POST API method
		Then book is successfully added

