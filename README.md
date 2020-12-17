# EntryPoint
- Developed a REST API entry point
- Using Python develop a REST Entry point service that provides a single endpoint.
## Requirements to run API
1. PyMySQL
2. Flask
## To access entry point Application use HTML pages 
1. entryP.html provides lookup for genes in database and gives four specific fields
- gene names (display_label field)
- location (location field)
- Ensembl stable ID (stable_id field)
- species (species field)
If Submitted parameter is not be under 3 chars (If submitted with less than 3 character, an
error code is returned (400 HTTP code))

2. check.html for the Some Business Rules
Service answer on GET queries, other queries (POST/PUT/PATCH) returns an error (405 HTTP code)
## Output Images
[Images](Images/)
