Summary:	Jakarta Commons Modeler
Name:		jakarta-commons-modeler
Version:	1.0
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-commons/release/commons-modeler/v%{version}/commons-modeler-%{version}-src.tar.gz
URL:		http://jakarta.apache.org/
Requires:	jre
BuildRequires:	jakarta-ant
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Jakarta Commons Modeller.

%package doc
Summary:	Jakarta Commons Modeller
Group:		Development/Languages/Java

%description doc
Jakarta Commons Modeller.

%prep
%setup -q -n commons-modeler-%{version}-src

%build
touch LICENSE
cp build.xml build.xml.org
sed -e 's#../LICENSE#LICENSE#g' build.xml.org > build.xml
ant dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install dist/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/LICENSE
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs
