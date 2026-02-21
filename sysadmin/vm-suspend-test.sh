#! /bin/ash
# VM SUSPEND TEST
#

rm -f /tmp/listid
touch /tmp/listid


######## Listing the running vms################
esxcli vm process list |grep -v "^\s.*"| grep -v "^$" > /tmp/list

########## cleaning the id.s file by keeping only the id
for name in `cat list`;do
        vim-cmd vmsvc/getallvms | grep $name | grep vmx | grep -v "^$" | awk '{print $1 }' >> /tmp/listid
done

for id in `cat /tmp/listid`;do
        ###### suspending vms##########
        echo "Suspending the running machines: "
        vim-cmd vmsvc/power.suspend $id
done

for id in `cat /tmp/listid`;do
        ###### Powering on vms##########
        echo "Powering on machines: "
        vim-cmd vmsvc/power.on $id
done


###### removing files############
#
rm /tmp/list
rm /tmp/listid
