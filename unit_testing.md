# Unit Testing

## Why?
* What does a codebase actually do?
    * I'd argue only what the test suite says it does
    * If its not tested, there really is no idea as to what that piece of code really does. There be dragons...
* Ensure that different parts of the larger application will work together.
* Ensure that future changes don't break existing code.
* Especially important in untyped/dynamic languages like Python and JS
    * Java/C++/golang will all complain if you try to do something silly.

## Good unit tests
* #####MOST IMPORTANT THINGS
    * _fixed well understood input -> fixed well understood output_
    * Isolation, should not hit any other services or make external calls
    * should be fast
* One to a few asserts per tests
    * Should test one single action (ideally)
        - Example -> Angular Component button click test
            ```
            handler() {
                this.loading = true;
                this.SomeService.getThings().then( (resp)-> {
                    this.things = resp;
                    this.loadMoreThings();
                }, (err)=>{
                    this.errorMessage = "No things"
                }).finally( ()=> {
                    this.loading = false;
                })
            }

            it("Should call the handler function on button click", ()=>{
                ctrl.handler();
                expect(ctrl.loading).toBe(false);
                expect(SomeService.getThings).toHaveBeenCalled();
                expect(ctrl.loadMoreThings).toHaveBeenCalled();
                expect(ctrl.things).toBe(themThangs);
            })

            ```
* Have descriptive names / error Messages
    - Failures should be clear in the log output.
        * someTest failed
        * someTest expected 3 but returned 4 with input of 9
            * expect(val).toEqual(3, "expected 3 but returned 4 with input of 9")

* Avoid if/else in the tests
    ```
        val = SomeClass.myOperation(42)
        if (val > 10):
            self.assertTrue(val == something)
        else:
            self.assertTrue(val == somethingElse )
    ```
    * Real hard to tell if the else statement ever gets hit
    * Break into 2 unit tests

* Test different flavors of inputs!
    *  `3, 33, -3, a, 1233453464575675675675675`
    * Example:
        - Agave job submission with spaces in filenames
    * This is where I think we could make some progress

* Refactor when needed!
    * Testing is part of writing code, think about testability when writing code
    * It should be pretty straight forward to write the tests.
    * If some code is a nightmare to test, it probably needs to be refactored.
        * Hard to reach code paths
        * Too many mocks
            * Basically a test of how well you can mock things...
        * Too many things to setup in the tests

## Run the tests locally first!
#### Viewing Results / Code Coverage
* `npm run test`
* `docker exec -e DJANGO_SETTINGS_MODULE=portal.settings.unit_test_settings -it cep_prtl_django coverage run --source="." manage.py test -v1 --pattern="unit_test.py"`
* `docker exec cep_prtl_django coverage html -i`
 
    * Look at line coverage. If it is not covered, the test suite never hit it.
    * Aim for 100%!
        * But more importantly aim to make good unit tests, 100% coverage with bad unit tests is even more dangerous.


Don't submit PR until it is ready. 2x the number of tests run, one for the original branch, one for the merged code. Saves minutes and electricity and C02.
