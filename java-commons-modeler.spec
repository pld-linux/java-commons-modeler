Summary:	Jakarta Commons Modeler - managing resources via Java Management Extensions
Summary(pl):	Jakarta Commons Modeler - zarz±dzanie zasobami z u¿yciem Java Management Extensions
Name:		jakarta-commons-modeler
Version:	1.0
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-commons/release/commons-modeler/v%{version}/commons-modeler-%{version}-src.tar.gz
# Source0-md5:	4a7f9e90ad74895a7e3d0acb2eb23572
URL:		http://jakarta.apache.org/
BuildRequires:	jakarta-ant
BuildRequires:	jdk >= 1.2
BuildRequires:	jmx
BuildRequires:	jakarta-commons-digester
BuildRequires:	jakarta-commons-logging
Requires:	jakarta-commons-beanutils
Requires:	jakarta-commons-collections
Requires:	jakarta-commons-digester
Requires:	jakarta-commons-logging
Requires:	jmx
Requires:	jre >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
This scope of the Modeler component is to provide a class library
supporting the creation and use of Model MBeans to manage application
resources via tools that implement the Java Management Extensions
(JMX) APIs.

%description -l pl
Zadaniem komponentu Modeler jest dostarczenie biblioteki klas
wspieraj±cych tworzenie i u¿ywanie Model MBeans do zarz±dzania
zasobami aplikacji z u¿yciem narzêdzi bêd±cych implementacj± API Java
Management Extensions (JMX).

%package doc
Summary:	Jakarta Commons Modeller documentation
Summary(pl):	Dokumentacja do Jakarta Commons Modeller
Group:		Development/Languages/Java

%description doc
Jakarta Commons Modeller documentation.

%description doc -l pl
Dokumentacja do Jakarta Commons Modeller.

%prep
%setup -q -n commons-modeler-%{version}-src

%build
cat << EOF > build.properties
commons-digester.jar=%{_javalibdir}/commons-digester.jar
commons-logging.jar=%{_javalibdir}/commons-logging.jar
jmx.jar=%{_javalibdir}/jmxri.jar
jmxtools.jar=%{_javalibdir}/jmxtools.jar
EOF
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
