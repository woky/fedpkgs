%global upstream_name PixivUtil2
%global upstream_version 20151117
%global upstream_release beta1
%global tarball_name %upstream_name-%upstream_version-%upstream_release

Name: %upstream_name
Version: %upstream_version
Release: 0.1.%upstream_release%{?dist}
Summary: Download images from Pixiv and more!

Group: Applications/Internet
License: BSD
URL: https://github.com/Nandaka/PixivUtil2
Source0: https://github.com/Nandaka/%name/archive/v%version-%upstream_release.tar.gz#/%tarball_name.tar.gz
Source1: PixivUtil2
Patch0: workdir.patch

BuildArch: noarch
BuildRequires: python2-devel
Requires: python-mechanize
Requires: python-BeautifulSoup
# The README says it requires socksipy-branch 1.02+.
Requires: python-SocksiPy
Requires: python-pillow

%description
Download images from Pixiv and more! http://nandaka.wordpress.com

%prep
%autosetup -n %tarball_name

%build

%install
install -D -m 644 Pixiv*.py -t %buildroot%python2_sitelib
install -D -m 755 %SOURCE1 -t %buildroot%_bindir

%files
%doc readme.txt changelog.txt
%python2_sitelib/Pixiv*.py{,c,o}
%_bindir/PixivUtil2

%changelog
* Wed Dec 16 2015 woky - 20151117-0.1.beta1
- Initial RPM release
