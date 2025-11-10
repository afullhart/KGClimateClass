Hello, thanks for considering our paper and we hope that it is within scope.

**Suggested Reviewers**

From the [Five most similar historical JOSS papers](https://github.com/openjournals/joss-reviews/issues/9375#issuecomment-3499478509), the top two papers are the best fit. In my opinion, the most important thing is knowledge of GEE and climate is secondary. Here's the suggested reviewer list:
* arbennett, usethedata, martibosch, kmarkert, aazuspan

This recently published GEE-related [paper](https://github.com/openjournals/joss-reviews/issues/8164) is also relevant but the reviewers are not in the database.

**Submission Checklist**

[x] OSI-approved license
[x] Installation instructions
* The GitHub Repo has a section called [Setup](https://github.com/ARS-SWRC/GEE-KGCC/tree/main?tab=readme-ov-file#setup) that provides instructions for installation and importing the developed package. This header was used instead of "Installation Instructions" because it provides both installation and importing instructions. We can change this heading if necessary.

[x] Documentation exists at all
* The GitHub Repo has documentation for the developed package under [Usage Notes](https://github.com/ARS-SWRC/GEE-KGCC/tree/main?tab=readme-ov-file#usage-notes). Because the package has relatively few functions, there is room for this documentation.

[x] Tests of some sort
* The [Test Example](https://github.com/ARS-SWRC/GEE-KGCC/tree/main?tab=readme-ov-file#test-example) is a python notebook that may be used for testing. In this case, because manual GEE authentication steps are already necessary in order to import the package, we opted to make the the entire test a manual test instead of automatic.

[ ] Check paper
[x] Substantial scholarly effort
* While the developed package is minimal because of its limited goal of KG classification, the web app represents a substantial effort. In my opinion, the web app is more polished than the average GEE app. It is possible for a user to copy/paste the app's code into the GEE platform and launch their own private instance of the app, such that it is not nessecary to visit our URL to use the app.

[x] Clear research application
* A number of extremely well cited papers have presented KGCC maps, and this package has the potential to apply KGCC to many publicaly accessible climate datasets.

