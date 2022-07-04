# check the ulist versions first
check_version() {
        local pp="../ulist/python/ulist/__init__.py"
        local pd="../docs/conf.py"
        local pc="../ulist/Cargo.toml"
        local vp=$(grep "__version" $pp | awk '{print $NF}' | sed 's/"//g')
        local vd=$(grep "release = " $pd | awk '{print $NF}' | sed "s/'//g")
        local vc=$(grep "version = " $pc | head -1 | awk '{print $NF}' | sed 's/"//g')
        if [ $vp != $vd -o $vp != $vc ]; then
                echo "Ulist versions don't match!"
                echo "$pp: $vp"
                echo "$pd: $vd"
                echo "$pc: $vc"
                echo "\n"
                return 1
        fi
        return 0
}

