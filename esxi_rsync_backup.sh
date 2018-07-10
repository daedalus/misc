#!/bin/sh
# Autor Dario Clavijo 2018
#set -x
DST=/vms/volumes/$1
                                        
echo "*-delta.vmdk" > /tmp/rsync_exclude
echo "*.vmsn" >> /tmp/rsync_exclude     
echo "*.lck >> /tmp/rsync_exclude"      
echo "*.log >> /tmp/rsync_exclude"      
                                                                                
# instalamos el binario de rync estatico                         
cd /tmp/               
wget https://damiendebin.net/files/esxi-static-rsync-3-1-0.tar.gz -O /tmp/esxi-static-rsync.tar.gz 
tar vxf /tmp/esxi-static-rsync.tar.gz
mv /tmp/rsync-static /bin/rsync                                                      
                                                                                
VMS=$(vim-cmd vmsvc/getallvms | awk '{ if(NR>1) print $1 }')                    
                                                                                
for VMID in $VMS                                                                
do                                                                              
    echo "VMID: $VMID"                                      
                                                            
    VMPATHNAME=$(vim-cmd vmsvc/get.summary $VMID | grep -e vmPathName)
    DATASTORE=$(echo $VMPATHNAME | awk '{ print $3 }' | sed 's/[^a-zA-Z0-9]//g')
    VMPATHDIR=$(echo $VMPATHNAME | awk '{ print $4 }' | sed -e 's/\// /g' | awk '{ print $1 }')
    VMPATH="/vmfs/volumes/$DATASTORE/$VMPATHDIR/"                                              
    echo $VMPATH                                                                               
                                                                                               
    # hacemos el snapshot de la VM con quiesce sin imagen de la RAM                            
    vim-cmd vmsvc/snapshot.create $VMID backup backup 0 1                                      
    SNAPSHOT_ID=$(vim-cmd vmsvc/snapshot.get $VMID | grep -e "Id" | awk '{  print $4 }')       
                                                                                               
    # se hace el backup backup                                                                 
    /bin/rsync --list-only --exclude-from=/tmp/rsync_exclude $VMPATH                    
                                                                                        
    # se borra el snapshot                                                              
    #vim-cmd vmsvc/snapshot.remove $VMID $SNAPSHOT_ID                                   
    vim-cmd vmsvc/snapshot.removeall $VMID                                              
done                                                                                    
rm /tmp/rsync_exclude 
