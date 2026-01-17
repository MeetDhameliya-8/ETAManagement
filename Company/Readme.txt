

i have worked the on the ETM management project and below i have described the detail/purpose of every subfolder:

1] Profile

        -->   to separate per role with rolebase permission and to provide each role theire own fields to save theire data 
              and to track theire work i have created this subprojec folder 
            
        -->   as we can see there are total 6 roles with each one sharing different purposes 

                after doing signup the flow begins to work 

                    1]NewJoine -  we have given a newjoinee form to the user after filling up that form with reasonable data the details go to HR and when 
                                  HR selects the user it joins the organization the gets the instrctions from senior regarding how to move forward after selecting field...
                    
                    2]Intern   -  interns gets the field in which we can track who has assigned the role and on which task he is working  

                    3]Employee -  from employee model fields like salary, phone,bio,Part of which projects he is, who is the assigner and 
                                  team members of that project also the detail of his previous company

                    4]HR       -  details about position of HR and in which department he is also about how many candidates he has managed and of 
                                  which employee's details comes under him as well about can he hire or not.

                    5]Manager  -  from manager details About the department and his project team can be seen.

                    6]Owner    -  the skills and the completed project as well as experience can be seen.
    
    # intern gets selected for new project by manager and gets small task from team as well daily task update in his own domain 



2] Requests 

        -->   here i have created the model named hrrequests and used foreignkey to bind it with newjoinee so the details from submitting the form will be shown to only HR.      
        -->   only HR, Manager and owner is capable of view the details of Applicants here.


3] Projects

sole purpose of creating this folder is to divide the work between team members from dashboard by manager.  

        -->   Project and task model are only visible to manager and can be only updated by manager 
        -->   EmployeeUpdate, InternUpdate, NewJonineeUpdate and HrUpdate Are the table to just provide the update by Admin and manager related to work. 
              i have created an forms to load the info from panel to domain.
        -->   so that An indivisual role can see theire task directly in domain 

                    ------------------------------------------------------------------------------------------------------------------------------------------------------
                    Functions                                                            
                    ------------------------------------------------------------------------------------------------------------------------------------------------------
                     
                    there are 4 functions 
                    which are to deliver the 
                    update from panel to template 

                    -> employee_update_view
                    -> intern_update_view 
                    -> newjoinee_update_view
                    -> hr_update_view 

                    --------------------------------
                    dashboard functions
                    --------------------------------

                    and 7 view functions are to 
                    operate with manager's action 
                    which are to add project and 
                    task with members 

                    -> create_project                                                                                                 
                    -> manager_dashboard
                    -> projects_dashboard
                    -> assign_members
                    -> project_detail 
                    -> add_task
                    -> my_projects 

                    with that i have used manager_required & 
                    login_required decorators here to make 
                    sure each function checks the if requests are 
                    coming from manager 
                    and login_required to see if user is logined 


                    here each view functions is working with POST method to create new update 
            

4] Interactions

        -->   to solve the issue of one way communication i have applied the idea of Interactions 

        -->   here user can share the Questions/ideas/Doubts by filling the mini form below update which he receives from panel 
              this helps to share ideas About topic.

        -->   for this purpose i have created an form and table named communication
    

5] Screensite 

        --> it's the domain folder which just has the authentication and rendering system working right newjoinee
        --> sign_up and login_views are working  on storing the details of new users 
        --> the one who sign_up goes to form to fill details 

        in login view if user's manager then instead of userdomain he will be automatically 
        get redirect to manager's dashboard

        --> there is also an logout_view function which is to redirect user out of domain 
        only working in manager dashboard





  ⚠ Info : 
    
        - confirmation and info template are currently no active since they have no purpose 
          right now and same goes for YOUR TASK button whiich appears on home page.

        that's why view functions related to these are not Active  
