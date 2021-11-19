FROM konstin2/maturin

# if you forked ulist, you can pass in your own GitHub username to use your fork
# i.e. gh_username=myname
ARG gh_username=tushushu
ARG ulist_home="/home/ulist"
ARG version = "0.1.0"
ARG branch="release-$version"

# Clone ulist repo
RUN mkdir "$ulist_home" \
    && git clone "https://github.com/$gh_username/ulist.git" "$ulist_home" \
    && cd "$ulist_home" \
    && git fetch \
    && git checkout "$branch"

# Build
RUN cd "$ulist_home/ulist" \
    && maturin build --release

# Run bash
ENTRYPOINT /bin/bash
