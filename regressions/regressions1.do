/*regressions*/




clear all
set more off
set matsize 800


cd "C:\Users\Adam\Google Drive\School\ComputerScience\intro to data science\Project_IMDB\stata"
use "movieData_1.dta"

gen rating100 = rating*10

local filename "regs1.xls"
local xs metascore rating100 rating_count critic_review_count avg_rating_per_demoaged_1829 ///,
avg_rating_per_demoaged_3044 avg_rating_per_demoaged_45 avg_rating_per_demoaged_under_18

local switch "replace"
local flags "dec(3) fmt(gc) nocons"

foreach var of local xs {

	reg gross_income `var' 
	outreg2 using `filename', `switch' `flags'
	local switch "append"

	reg gross_income `var' budget
	outreg2 using `filename', `switch' `flags'

	reg gross_income `var' budget avg_screens
	outreg2 using `filename', `switch' `flags'
	
	reg gross_income `var' budget duration
	outreg2 using `filename', `switch' `flags'
	
}
