source department.sql
source employee.sql
source project.sql
source dept_locations.sql
source dependent.sql
source worksOn.sql

set foreign_key_checks = 0;

source load-department.sql
source load-employee.sql
source load-project.sql
source load-dloc.sql
source load-dependent.sql
source load-worksOn.sql

set foreign_key_checks = 1;
