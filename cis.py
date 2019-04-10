import re

def test_audit_1_1_1_1_a(host):
    r = host.run('modprobe -n -v cramfs')
    assert re.match(r'install /bin/true', r.stdout) is not None

def test_audit_1_1_1_1_b(host):
    r = host.run('lsmod | egrep cramfs')
    assert re.match(r'^$', r.stdout) is not None

def test_audit_1_1_1_2_a(host):
    r = host.run('modprobe -n -v freevxfs')
    assert re.match(r'install /bin/true', r.stdo is not Noneut)

def test_audit_1_1_1_2_b(host):
    r = host.run('lsmod | egrep freevxfs')
    assert re.match(r'^$', r.stdout) is not None

def test_audit_1_1_1_3_a(host):
    r = host.run('modprobe -n -v jffs2')
    assert re.match(r'install /bin/true', r.stdout) is not None

def test_audit_1_1_1_3_b(host):
    r = host.run('lsmod | egrep jffs2')
    assert re.match(r'^$', r.stdout) is not None

def test_audit_1_1_1_4_a(host):
    r = host.run('modprobe -n -v hfs')
    assert re.match(r'install /bin/true', r.stdout) is not None

def test_audit_1_1_1_4_b(host):
    r = host.run('lsmod | egrep hfs')
    assert re.match(r'^$', r.stdout) is not None

def test_audit_1_1_1_5_a(host):
    r = host.run('modprobe -n -v hfsplus')
    assert re.match(r'install /bin/true', r.stdout) is not None

def test_audit_1_1_1_5_b(host):
    r = host.run('lsmod | egrep hfsplus')
    assert re.match(r'^$', r.stdout) is not None

def test_audit_1_1_1_6_a(host):
    r = host.run('modprobe -n -v squashfs')
    assert re.match(r'install /bin/true', r.stdout) is not None

def test_audit_1_1_1_6_b(host):
    r = host.run('lsmod | egrep squashfs')
    assert re.match(r'^$', r.stdout) is not None

def test_audit_1_1_1_7_a(host):
    r = host.run('modprobe -n -v udf')
    assert re.match(r'install /bin/true', r.stdout) is not None

def test_audit_1_1_1_7_b(host):
    r = host.run('lsmod | egrep udf')
    assert re.match(r'^$', r.stdout) is not None

def test_audit_1_1_1_8_a(host):
    r = host.run('modprobe -n -v vfat')
    assert re.match(r'install /bin/true', r.stdout) is not None

def test_audit_1_1_1_8_b(host):
    r = host.run('lsmod | egrep vfat')
    assert re.match(r'^$', r.stdout) is not None

def test_audit_1_1_2(host):
    r = host.run('mount | egrep /tmp[^/]')
    assert re.match(r'.* on /tmp', r.stdout) is not None

def test_audit_1_1_3(host):
    r = host.run('mount | egrep /tmp[^/]')
    assert re.match(r'.* on /tmp type tmpfs (.*nodev.*)', r.stdout) is not None

def test_audit_1_1_4(host):
    r = host.run('mount | egrep /tmp[^/]')
    assert re.match(r'.* on /tmp type tmpfs (.*nosuid.*)', r.stdout) is not None

def test_audit_1_1_5(host):
    r = host.run('mount | egrep /tmp[^/]')
    assert re.match(r'.* on /tmp type tmpfs (.*noexec.*)', r.stdout) is not None

def test_audit_1_1_6(host):
    r = host.run('mount | egrep /var[^/]')
    assert re.match(r'.* on /var', r.stdout) is not None

def test_audit_1_1_7(host):
    r = host.run('mount | egrep /var/tmp[^]')
    assert re.match(r'.* on /var/tmp type ext4', r.stdout) is not None

def test_audit_1_1_8(host):
    r = host.run('mount | egrep /var/tmp[^]')
    assert re.match(r'.* on /tmp type ext4 (.*nodev.*)', r.stdout) is not None

def test_audit_1_1_9(host):
    r = host.run('mount | egrep /var/tmp[^]')
    assert re.match(r'.* on /tmp type ext4 (.*nosuid.*)', r.stdout) is not None

def test_audit_1_1_10(host):
    r = host.run('mount | egrep /var/tmp[^]')
    assert re.match(r'.* on /tmp type ext4 (.*noexec.*)', r.stdout) is not None

def test_audit_1_1_11(host):
    r = host.run('mount | egrep /var/log[^]')
    assert re.match(r'.* on /var/log type ext4', r.stdout) is not None

def test_audit_1_1_12(host):
    r = host.run('mount | egrep /var/log/audit[^]')
    assert re.match(r'.* on /var/log/audit type ext4', r.stdout) is not None

def test_audit_1_1_13(host):
    r = host.run('mount | egrep /home[^/]')
    assert re.match(r'.* on /home type ext4', r.stdout) is not None

def test_audit_1_1_14(host):
    r = host.run('mount | egrep /home[^/]')
    assert re.match(r'.* on /home type ext4 (.*nodev.*)', r.stdout) is not None

def test_audit_1_1_15(host):
    r = host.run('mount | egrep /dev/shm[^/]')
    assert re.match(r'.* on /home type ext4 (.*nodev.*)', r.stdout) is not None

def test_audit_1_1_15(host):
    r = host.run('mount | egrep /dev/shm[^/]')
    assert re.match(r'.* on /home type ext4 (.*nodev.*)', r.stdout) is not None

def test_audit_1_1_16(host):
    r = host.run('mount | egrep /dev/shm[^/]')
    assert re.match(r'.* on /home type ext4 (.*nosuid.*)', r.stdout) is not None

def test_audit_1_1_17(host):
    r = host.run('mount | egrep /dev/shm[^/]')
    assert re.match(r'.* on /home type ext4 (.*noexec.*)', r.stdout) is not None

def test_audit_1_1_18(host):
    assert False, "Check by yourself"

def test_audit_1_1_19(host):
    assert False, "Check by yourself"

def test_audit_1_1_20(host):
    assert False, "Check by yourself"

def test_audit_1_1_21(host):
    r = host.run(" df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d \( -perm -0002 -a ! -perm -1000 \) 2>/dev/null")
    assert re.match(r'^$', r.stdout) is not None

def test_audit_1_1_22(host):
    r = host.run('systemctl is-enabled autofs')
    assert re.match(r'disabled', r.stdout) is not None
