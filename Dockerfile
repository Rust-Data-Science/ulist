FROM konstin2/maturin

# if you forked ulist, you can pass in your own GitHub username to use your fork
# i.e. gh_username=myname
ARG gh_username=tushushu
ARG ulist_home="/home/ulist"

# Clone ulist repo
RUN mkdir "$ulist_home" \
    && git clone "https://github.com/$gh_username/ulist.git" "$ulist_home" \
    && cd "$ulist_home"

# Unit tests
RUN Python test.py

# Build ulist
RUN cd "ulist" && maturin build --release
