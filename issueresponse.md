Hello, thanks for considering our paper and we hope that it is within scope. I will provide details on suggested reviewers and remaining checklist items. At this stage, I'm unclear whether I should attempt to correct the remaining issues with the paper (a few issues have been realized, listed below). For now, I'll leave as is.

**Suggested Reviewers**

From the [Five most similar historical JOSS papers](https://github.com/openjournals/joss-reviews/issues/9375#issuecomment-3499478509), the top two papers are the best fit. In my opinion, the most important thing is knowledge of GEE and climate is secondary. Here's the suggested reviewer list:
* arbennett, usethedata, martibosch, kmarkert, aazuspan

This recently published GEE-related [paper](https://github.com/openjournals/joss-reviews/issues/8164) is also relevant but the reviewers are not in the database.

**Submission Checklist**

[x] OSI-approved license

[x] Installation instructions
* The GitHub Repo has a section called [Setup](https://github.com/ARS-SWRC/GEE-KGCC/tree/main?tab=readme-ov-file#setup) that provides instructions for installation and importing the developed package. This heading was used instead of "Installation Instructions" because both installation and importing instructions are provided. We can change this heading title if necessary.

[x] Documentation exists at all
* The GitHub Repo has documentation for the developed package under [Usage Notes](https://github.com/ARS-SWRC/GEE-KGCC/tree/main?tab=readme-ov-file#usage-notes). Because the package has relatively few functions, there is room to document each function in the ReadMe document.

[x] Tests of some sort
* The [Test Example](https://github.com/ARS-SWRC/GEE-KGCC/tree/main?tab=readme-ov-file#test-example) is a python notebook that may be used for testing. In this case, because manual GEE authentication steps are already necessary in order to import the package, we opted to make the the entire test a manual test instead of automatic.

[ ] Check paper
* The DOIs were provided as hyperlinks, and I'm guessing this is why editorialbot is flagging them. We can take out the hyperlinks if that would solve the problem.
* The list of app features under the "Web application" section was intended to be bullet points. We will fix this formatting issue.
* The paper length is considerably longer than 1000 words, and we can take steps to reduce the paper length if it is determined to be necessary.

[x] Substantial scholarly effort
* While the developed package is minimal because of its limited goal of KG classification, the web app represents a substantial effort. In my opinion, the web app is more polished than the average GEE app. It is possible for a user to copy/paste the app's code into the GEE platform and launch their own private instance of the app, such that it is not nessecary to visit our URL to use the app.

[x] Clear research application
* A number of extremely well cited papers have presented KGCC maps, and this package has the potential to apply KGCC to many publicaly accessible climate datasets.
