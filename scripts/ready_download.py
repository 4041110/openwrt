#=================================================
# Description: Build OpenWrt using GitHub Actions
# Author: sirpdboy
# https://github.com/sirpdboy/Openwrt
#!/bin/bash
git clone https://github.com/coolsnowwolf/lede.git openwrt
cd openwrt
git clone https://github.com/siropboy/mypackages package/mypackages
git clone https://github.com/siropboy/mysmall package/mysmall
./scripts/feeds update -a
mkdir  ../bak
mv ./feeds/luci/modules/luci-mod-admin-full/luasrc/view/admin_system/poweroff.htm  ../bak
mv ./feeds/luci/modules/luci-mod-admin-full/luasrc/controller/admin/system.lua   ../bak
mv ./package/lean/default-settings/files/zzz-default-settings   ../bak
mv ./package/lean/autocore/files/index.htm  ../bak
mv ./package/lean/autocore/files/cpuinfo  ../bak
sed -i 's/= "unreachable"/= "default"/g' feeds/luci/applications/luci-app-mwan3/luasrc/model/cbi/mwan/policyconfig.lua
sed -i 's/������/���/g' feeds/luci/applications/luci-app-nlbwmon/po/zh-cn/nlbwmon.po
wget -P  ./feeds/luci/modules/luci-mod-admin-full/luasrc/view/admin_system https://raw.githubusercontent.com/siropboy/other/master/patch/poweroff/poweroff.htm 
wget -P  ./feeds/luci/modules/luci-mod-admin-full/luasrc/controller/admin https://raw.githubusercontent.com/siropboy/other/master/patch/poweroff/system.lua 
wget -P package/lean/default-settings/files  https://raw.githubusercontent.com/siropboy/other/master/patch/default-settings/zzz-default-settings
sed -i 's/ʵʱ�������/���/g' package/lean/luci-app-wrtbwmon/po/zh-cn/wrtbwmon.po
sed -i 's/����洢/�洢/g' package/lean/luci-app-vsftpd/po/zh-cn/vsftpd.po
sed -i 's/Turbo ACC �������/ACC�������/g' package/lean/luci-app-flowoffload/po/zh-cn/flowoffload.po
sed -i 's/Turbo ACC �������/ACC�������/g' package/lean/luci-app-sfe/po/zh-cn/sfe.po
sed -i 's/���������ƻ�ɫ����/������ɫ����/g' package/lean/luci-app-unblockmusic/po/zh-cn/unblockmusic.po
sed -i 's/��ͥ��//g' package/lean/luci-app-familycloud/luasrc/controller/familycloud.lua
#sed -i '/filter_aaaa/d' package/network/services/dnsmasq/files/dhcp.conf
sed -i 's/$(VERSION_DIST_SANITIZED)/$(shell date +%Y%m%d)-$(VERSION_DIST_SANITIZED)/g' include/image.mk
wget -P package/lean/autocore/files  https://raw.githubusercontent.com/siropboy/other/master/patch/autocore/files/index.htm
wget -P package/lean/autocore/files https://raw.githubusercontent.com/siropboy/other/master/patch/autocore/files/sbin/cpuinfo
./scripts/feeds install -a

cd ../
exit 0