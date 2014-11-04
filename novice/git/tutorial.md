--- 
layout: lesson 
root: ../..
title: Version Control
---

Tracking your changes with a local repository
---------------------------------------------

Version control is centred round the notion of a *repository* which
holds your directories and files. We'll start by looking at a local
repository. The local repository is set up in a directory in your local
filesystem (local machine).

### Create a new repository with Git

We will be working with a simple example in this tutorial. It will be a
paper that we will first start writing as a single author and then work
on it further with one of our colleagues. 

 First, let's create a directory:

     
       $ mkdir papers 
       $ cd papers

Now, we need to set up this directory up to be a Git repository (or
"initiate the repository"):

       $ git init
    Initialized empty Git repository in /home/user/papers/.git/

The directory "papers" is now our working directory. 

 If we look in this directory, we'll find a *.git* directory:

      $ ls -a
    .git:
    branches  config  description  HEAD  hooks  info  objects  refs

.git directory contains Git's configuration files. Be careful not to
accidentally delete this directory!

### Tell Git who we are

As part of the information about changes made to files Git records who
made those changes. In teamwork this information is often crucial (do
you want to know who rewrote your 'Conclusions' section?). So, we need
to tell Git about who we are,

     
    $ git config --global user.name "Your Name"
    $ git config --global user.email "yourname@yourplace.org"

### Set a default editor

When working with Git we will often need to provide some short but
useful information. In order to enter this information we need an
editor. We'll now tell Git which editor we want to be the default one
(i.e. Git will always bring it up whenever it wants us to provide some
information). \
 You can choose any available in you system editor. For the purpose of
this session we'll use nano:

    $ git config --global core.editor nano

To set up vi as the default editor:

     
    $ git config --global core.editor vi

### Git's global configuration

We can now preview (and edit, if necessary) Git's global configuration
(such as our name and the default editor which we just set up). If we
look in our home directory, we'll see a .gitconfig file,

    $ cat ~/.gitconfig
    [user]
    name = Your Name 
    email = yourname@yourplace.org 
    [core] 
    editor = nano

This file holds global configuration that is applied to any Git
repository in your file system.

### Add a file to the repository

Now, we'll create a file. Let's say we're going to write a journal
paper:

    $ nano journal.txt

and add headings for Title, Author, Introduction, Conclusion and
References, and save the file.\
 git status allows us to find out about the current status of files in
the repository. So, we can run,

    $ git status journal.txt

Information about what Git knows about the file is displayed. For now,
the important bit of information is that our file is listed as Untracked
which means it's in our working directory but Git is not tracking it -
that is, any changes made to this file will not be recorded by Git. To
tell Git about the file, we will use the *add* command:

    $ git add journal.txt
    $ git status journal.txt
    
Now, our file is now listed as one of some Changes to be committed. 
    
*git add* is used for two purposes. Firstly, to tell Git that a given file should be tracked. Secondly, to put the file into the Git's **staging area** which is also known as the index or the cache. 

The staging area can be viewed as a "loading dock", a place to hold files
we've added, or changed, until we're ready to tell Git to record those
changes in the repository.  

 In order to tell Git to record our change, our new file, into the
repository, we need to commit it:

    $ git commit

Our default editor will now pop up. Why? Well, Git can automatically
figure out that directories and files are committed, and who by (thanks
to the information we provided before) and even, what changes were made,
but it cannot figure out why. So we need to provide this in a commit
message. So let's type in a message. "Initial structure and headings for
the journal paper." 



 Ideally, commit messages should have meaning to others who may read
them - or you 6 months from now. Messages like "made a change" or "added
changes" or "commit 5" aren't that helpful (in fact, they're
redundant!). A good commit message usually contains a one-line
description followed by a longer explanation, if necessary. 

 If we save our commit message, Git will now commit our file.

     [master (root-commit) c381e68] This is my journal paper.
     1 file changed, 9 insertions(+)
     create mode 100644 journal.txt

This output shows the number of files changed and the number of lines
inserted or deleted across all those files. Here, we've changed (by
adding) 1 file and inserted 9 lines. 

 Now, if we look at its status,

    $ git status journal.txt
    # On branch master
    nothing to commit (working directory clean)

nothing to commit means that our file is now in the repository, our
working directory is up-to-date and we have no uncommitted changes in
our staging area. 

 To see the history of changes that we made to our repository (the most
recent changes will be displayed at the top):

    $ git log

The output shows: the commit identifier (also called revision number)
which uniquely identifies the changes made in this commit, author, date,
and your comment. 

 Now let's make some more changes to our journal.txt file . If we now
run,

     $ git status journal.txt

we see changes not staged for commit section and our file is marked as
modified. This means that a file Git knows about has been modified by us
but has not yet been committed. So we can add it to the staging area and
then commit the changes:

     
    $ git add journal.txt
    $ git commit
    
Note that in this case we used "git add" to put journal.txt to the staging area. Git already knows this file should be tracked but doesn't know if we want to commit the changes we made to the file  in the repository and hence we have to add the file to the staging area. 

It can sometimes be quicker to provide our commit messages at the command-line by doing:

    $ git add journal.txt
    $ git commit -m "Added subsection headings." 

Let's add a directory, common and a file references.txt for references
we may want to reuse:

    $ mkdir common
    $ nano common/references.txt
    
We will also add a few lines to our paper (journal.txt). Now we need to record our work in the repository so we need to make a commit.
First we tell Git to track the references. We can actually tell Git to track everything in the given subdirectory:

    $ git add common

All files that are in "common" are now tracked.
We would also have to add journal.txt to the staging area. But there is a shortcut. We can use option "-a" for "commit". This option means "commit all files that are tracked and that have been modified".

    $ git commit -am "Added common directory and references file with Cohen et al reference and described data in the paper"

and Git will add, then commit, both the directory and the file.

### Looking at our history

To see the history of changes that we made to our repository (the most
recent changes will be displayed at the top):

     $ git log

Git automatically assigns an identifier (COMMITID) to each commit made
to the repository. In order to see the changes made between any earlier
commit and our current version, we can use git diff providing the commit
identifier of the earlier commit:

    $ git diff COMMITID

And, to see changes between two commits:

    $ git diff OLDER_COMMITID NEWER_COMMITID

Using our commit identifiers we can set our working directory to contain
the state of the repository as it was at any commit. So, let's go back
to the very first commit we made,

    $ git log
    $ git checkout COMMITID

We will get something like this:

    Note: checking out 'c4354a9c578aa5b81d354d8b3330fda7b9b23d3e'.

    You are in 'detached HEAD' state. You can look around, make experimental changes and commit them, and you can discard any commits you make in this state without impacting any branches by performing another checkout.

    If you want to create a new branch to retain commits you create, you may    do so (now or later) by using -b with the checkout command again. Example:
        git checkout -b new_branch_name

    HEAD is now at c4354a9... Added sections

*HEAD* is essentially a pointer which points to the branch where you
currently are. We said previously that *master* is the default branch. But
*master* is actually a pointer - that points to the tip of the master
branch (the sequence of commits that is created by default by Git). You may think of *master* as two things: one as a pointer and one as the default branch. 

When we checked out one of the past commits HEAD is pointing to that commit
but does not point to the same thing as master any more. That is why git
says You are in 'detached HEAD' state and advises us that if we want to
make a commit now, we should create a new branch to retain these
commits. 

If we created a new commit without creating a new branch Git
would not know what to do with it (since there is already a commit in
master branch from the current state which we checked out c4354a...). We
will get back to branches and HEAD pointer later in this tutorial. \
 If we look at journal.txt, we'll see it's our very first version. And
if we look at our directory,

    $ ls
    journal.txt

Our directory with the references is gone.But, rest easy, while it's
gone from our working directory, it's still in our repository. We can
jump back to the latest commit by doing:

    $ git checkout master

And common will be there once more,

    $ ls
    common journal.txt

So we can get any version of our files from any point in time. In other
words, we can set up our working directory back to any stage it was when
we made a commit.

 **Top tip: Commit often** 
 
 In the same way that it is wise to frequently save a document that you
are working on, so too is it wise to save numerous revisions of your
files. More frequent commits increase the granularity of your "undo"
button. 

 While DropBox and GoogleDrive also preserve every version, they delete
old versions after 30 days, or, for GoogleDrive, 100 revisions. DropBox
allows for old versions to be stored for longer but you have to pay for
this. Using revision control the only bound is how much space you have!

### Using tags as nicknames for commit identifiers

Commit identifiers are long and cryptic. Git allows us to create tags,
which act as easy-to-remember nicknames for commit identifiers. For
example,

    $ git tag VER_REVIEWED_BY_JOHN

We can list tags by doing:

    $ git tag

Now if we change our file,

    $ git add journal.txt
    $ git commit -m "..." journal.txt

We can checkout our previous version using our tag instead of a commit
identifier.

    $ git checkout VER_REVIEWED_BY_JOHN

Branching
---------

### What is a branch?

You might have noticed the term branch in status messages,

    $ git status journal.txt
    # On branch master
    nothing to commit (working directory clean)

and when we wanted to get back to our most recent version of the
repository, we used,

    $ git checkout master

Not only can our repository store the changes made to files and
directories, it can store multiple sets of these, which we can use and
edit and update in parallel. Each of these sets, or parallel instances,
is termed a branch and master is Git's default branch. 

 A new branch can be created from any commit. Branches can also be
merged together. 

 Why is this useful? Suppose we've developed some software and now we
want to add some new features to it but we're not sure yet whether we'll
keep them. We can then create a branch 'feature1' and keep our master
branch clean. When we're done developing the feature and we are sure
that we want to include it in our program, we can merge the feature
branch with the master branch. 
 
 We create our branch for the new feature.

    -c1---c2---c3                               master
                \
                 c4                             feature1

We can then continue developing our software in our default, or master,
branch,

     
    -c1---c2---c3---c5---c6---c7                   master
                \
                 c4                                feature1

And, we can work on the new feature in the feature1 branch

    -c1---c2---c3---c5---c6---c7                   master
                \
                 c4---c8---c9                      feature1

We can then merge the feature1 branch adding new feature to our master
branch (main program):

     -c1---c2---c3---c5---c6---c7--c10              master
                \                   /
                 c4---c8---c9------                 feature1

When we merge our feature1 branch with master git creates a new commit
which contains merged files from master and feature1. After the merge we
can continue developing. The merged branch is not deleted. We can
continue developing (and making commits) in feature1 as well.

    -c1---c2---c3---c5---c6---c7--c10---c11--c12     master
                \                /
                 c4---c8---c9-------c13              feature1

One popular model is to have,

-   A release branch, representing a released version of the code.
-   A master branch, representing the most up-to-date stable version of
    the code.
-   Various feature and/or developer-specific branches representing
    work-in-progress, new features etc.

For example,

               0.1      0.2        0.3
              c6---------c9------c17------            release
             /          /       /
     c1---c2---c3--c7--c8---c16--c18---c20---c21--    master
     |                      /
     c4---c10---c13------c15                          fred
     |                   /
     c5---c11---c12---c14---c19                       kate


There are different possible workflows when using Git for code development. 

One of the examples may be when the master branch holds stable and tested code.  If a bug is found by a user, a bug fix can be applied to the release branch, and then merged with the master branch. 
When a feature or developer-specific branch, is stable and has been reviewed and tested it can be merged with the master branch. When the master branch has been
reviewed and tested and is ready for release, a new release branch can
be created from it.
If you want to learn more about workflows with Git, have a look at the [AstroPy development workflow](http://astropy.readthedocs.org/en/latest/development/workflow/development_workflow.html).


### Branching in practice

One of our colleagues wants to contribute to the paper but it's not
quite sure if it will actually make a publication. So it will be safer
to create a branch and carry on working on this "experimental" version
of the paper in a branch rather than in the master.

    $ git checkout -b paperWJohn
    Switched to a new branch 'paperWJohn'

Now let's change the title of our paper and the autors (adding John
Smith). Let's commit our changes. Before we do that, it's a good
practice to check whether we're working in the correct branch.

    $ git branch
    * paperWJohn
      master

The * indicates which branch we're currently in. Let's commit. If we
want to work now in our master branch. We can switch by using:

    $ git checkout master 
    Switched to branch 'master'

### Merging and resolving conflicts

We are now working on two papers. Our main one in our master branch and
the one which may possibly be collaborative work in our "paperWJohn"
branch. Let's suppose that we have a new idea for the title for our main
paper. We can change it in our master branch. Let's do it and commit
changes.

    $ nano journal.txt
    ......
    $ git add journal.txt
    $ git commit -m "Rewrote the title" journal.txt

After some discussions with John we decided that there is going to be a
major change to our plan. We will publish together. And hence it makes
sense now to merge all that was authored together with John in branch
"paperWJohn". 

 We can do that by *merging* that branch with the master branch. Let's
try doing that:

    $ git merge paperWJohn
    Auto-merging journal.txt
    CONFLICT (content): Merge conflict in journal.txt
    Automatic merge failed; fix conflicts and then commit the result.

Git cannot complete the merge because there is a conflict - if you
recall, journal.txt differs in the same places (lines) in the master and
the paperWJohn branch. We have to resolve the conflict and then complete
the merge. Let's see a bit more details:

    $ git status
    # On branch master
    # You have unmerged paths.
    #   (fix conflicts and run "git commit")
    #
    # Changes to be committed:
    #
    # Unmerged paths:
    #   (use "git add ..." to mark resolution)
    #
    # both modified:      journal.txt
    #

Let's look inside journal.txt:

    <<<<<<< HEAD 
    Title: A paper about proteines
    =======
    Title: A paper about everything but proteines
    >>>>>>> 71d34decd32124ea809e50cfbb7da8e3e354ac26 

The mark-up shows us the parts of the file causing the conflict and the
versions they come from. We now need to manually edit the file to
resolve the conflict. This means removing the mark-up and doing one of:

-   Keep the local version, which, here, is the one marked-up by HEAD
    i.e. "Title: A paper about proteines"
-   Keep the remote version, which, here, is the one marked-up by the
    commit identifier i.e. "Title: A paper everything but proteines"
-   Or keep a combination of the two e.g. "Title: A paper about
    proteines and everything else"

We edit the file. Then commit our changes e.g.

    $ git add journal.txt
    $ git commit -m "Resolved conflict in journal.txt by rewriting title to combine best of both originals"

This is where version control proves itself better than DropBox or
GoogleDrive, this ability to merge text files line-by-line and highlight
the conflicts between them, so no work is ever lost.

Working from multiple locations with a remote repository
--------------------------------------------------------

We're going to set up a remote repository that we can use from multiple
locations. The remote repository can also be shared with colleagues, if
we want to.

### GitHub

[GitHub](http://GitHub.com) is a GitHub is a web-based hosting service which allows users to set up their private and public source code Git repositories. It provides
tools for browsing, collaborating on and documenting code. Your
organisation may also offer support for hosting Git repositories - ask
your local system administrator. GitHub, like other services such
as [Launchpad](https://launchpad.net),[Bitucket](http://bitbucket.org),
[GoogleCode](http://code.google.com), and
[SourceForge](http://sourceforge.net) provides a wealth of resources to
support projects including:

-   Time histories changes to repositories
-   Commit-triggered e-mails
-   Browsing code from within a web browser, with syntax highlighting
-   Software release management
-   Issue (ticket) and bug tracking
-   Download
-   Varying permissions for various groups of users
-   Other service hooks e.g. to Twitter.

**Note** 
GitHub's free repositories have public licences **by default**.
If you don't want to share (in the most liberal sense) your stuff with
the world and you want to use GitHub (instead of for exmple, BitBucket), you will need to pay for the private GitHub repositories (GitHub offers up to 5 free
private repositories, if you are an academic - but do check this
information as terms and conditions may change).

### Create a new repository

Now, we can create a repository on GitHub,

-   Log in to GitHub (if you don't have an account, set up one)
-   Click on the Create icon on the top right
-   Enter Repository name: "2014-06-PISA-YOURNAME"
-   For the purpose of this exercise we'll create a public repository
-   Make sure the Initialize this repository with a README is unselected
-   Click Create Repository

You'll get a page with new information about your repository. We already
have our local repository and we will be pushing it to GitHub.

    git remote add origin https://github.com/USERNAME/2014-06-PISA-YOURNAME.git
    git push -u origin master

This sets up an alias, origin, to correspond to the URL of our new
repository on GitHub. 

 Now copy and paste the second line

    $ git push -u origin master
    Counting objects: 38, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (30/30), done.
    Writing objects: 100% (38/38), 3.59 KiB, done.
    Total 38 (delta 9), reused 0 (delta 0)
    To https://github.com/USERNAME/2014-06-PISA-YOURNAME.git
    * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.

This pushes our master branch to the remote repository, named via the
alias origin and creates a new master branch in the remote repository. 

 Now, on GitHub, we should see our code and click the Commits tab we
should see our complete history of commits. 

 Our local repository is now available on GitHub. So, anywhere we can
access GitHub, we can access our repository.

### Cloning a remote repository

Now, let's do something drastic!

    $ cd ..
    $ rm -rf papers

We've just wiped our local repository! But, as we've a copy on GitHub we
can just copy, or clone that,

    $ git clone https://USERNAME@github.com/USERNAME/2014-06-PISA-YOURNAME.git
    Cloning into '2014-06-PISA-YOURNAME'...
    Password for 'https://USERNAME@github.com':
    remote: Counting objects: 12, done.
    remote: Compressing objects: 100% (4/4), done.
    remote: Total 12 (delta 0), reused 0 (delta 0)
    Unpacking objects: 100% (12/12), done.

Now, if we change into "2014-06-PISA-YOURNAME" we can see that we have
our repository,

    $ cd 2014-06-PISA-YOURNAME
    $ git log

and we can see our Git configuration files too,

    $ ls -A
    common  .git  journal.txt

But where is the papers directory, you might ask? papers was the
directory that held our local repository but was not a part of it.

### Push changes to a remote repository

We can use our cloned repository just as if it was a local repository so
let's make some changes to our files and commit these. 

 Having done that, how do we send our changes back to the remote
repository? We can do this by pushing our changes,

    $ git push

If we now check our GitHub page we should be able to see our new
changes. 

 Before you push to a remote repository you should always pull so you
have the most up-to-date copy of the remote repository. So, on that
note...

### Pull changes from a remote repository

We'll work in pairs now. Find a partner and clone each other's
repositories. Now each one of you should make some changes to the
"journal.txt" in *your* repository and push it to GitHub. How to get
your partner's latest changes now in the cloned repository? 

 One way is simply to clone the repository every time but this is
inefficient, especially if our repository is very large. So, Git allows
us to get the latest changes down from a repository by *pullling* them.


 To get the partner's changes, go to the repository you cloned from
their GitHub account:

     $cd 2014-06-PISA-YOUR-PARTNERS-NAME

And pull the changes

     $git pull 

Conclusions and further information
-----------------------------------

We've seen how we can use version control to,

-   Keep track of changes like a lab notebook for code and documents.
-   Roll back changes to any point in the history of changes to our
    files - "undo" and "redo" for files.
-   Back up our entire history of changes in various locations.
-   Work on our files from multiple locations.
-   Identify and resolve conflicts when the same file is edited within
    two repositories without losing any work.
-   Collaboratively work on code or documents or any other files.

Version control serves as a log book for your software and documents,
ideas you've explored, fixes you've made, refactorings you've done,
false paths you've explored - what was changed, who by, when and why -
with a powerful undo and redo feature! 

 It also allows you to work with others on a project, whether that be
writing code or papers, down to the level of individual files, without
the risk of overwriting and losing each others work, and being able to
record and understand who changed what, when, and why.

### More information
-    Karthik Ram (2013) "git can facilitate greater reproducibility and increased transparency in science", Source Code for Biology and Medicine 2013, 8:7 doi [10.1186/1751-0473-8-7](http://dx.doi.org/10.1186/1751-0473-8-7) survey of the range of ways in which version control can help research.
-   [Visual Git Reference](http://marklodato.github.com/visual-git-guide/index-en.html) - pictorial representations of what Git commands do.
-   [Pro Git](http://git-scm.com/book) - the "official" online Git book.
-   [Version control by example](http://www.ericsink.com/vcbe/) - an
    acclaimed online book on version control by Eric Sink.
 - [Git Branching](http://pcottle.github.io/learnGitBranching/) - interactive tutorial to practice branching
-   [Git commit
    policies](http://osteele.com/posts/2008/05/commit-policies) - images
    on what Git commands to with reference to the working directory,
    staging area, local and remote repositories.
-   [Gitolite](https://github.com/sitaramc/gitolite) - a way for you to
    host your own multi-user Git repositories. Your collaborators send
    you their public SSH keys then they can pull and push from/to the
    repositories.
    


