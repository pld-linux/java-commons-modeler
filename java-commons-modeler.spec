Summary:	Jakarta Commons Modeler - managing resources via Java Management Extensions
Summary(pl.UTF-8):   Jakarta Commons Modeler - zarządzanie zasobami z użyciem Java Management Extensions
Name:		jakarta-commons-modeler
Version:	1.1
Release:	1
License:	Apache v1.1
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/modeler/source/modeler-%{version}-src.tar.gz
# Source0-md5:	6de043186a348758c845f1a2321e8308
URL:		http://jakarta.apache.org/commons/modeler/
BuildRequires:	ant
BuildRequires:	jakarta-commons-digester
BuildRequires:	jakarta-commons-logging
BuildRequires:	jdk >= 1.2
BuildRequires:	jmx
Requires:	jakarta-commons-beanutils
Requires:	jakarta-commons-collections
Requires:	jakarta-commons-digester
Requires:	jakarta-commons-logging
Requires:	jmx
Requires:	jre >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This scope of the Modeler component is to provide a class library
supporting the creation and use of Model MBeans to manage application
resources via tools that implement the Java Management Extensions
(JMX) APIs.

%description -l pl.UTF-8
Zadaniem komponentu Modeler jest dostarczenie biblioteki klas
wspierających tworzenie i używanie Model MBeans do zarządzania
zasobami aplikacji z użyciem narzędzi będących implementacją API Java
Management Extensions (JMX).

%package doc
Summary:	Jakarta Commons Modeller documentation
Summary(pl.UTF-8):   Dokumentacja do Jakarta Commons Modeller
Group:		Development/Languages/Java

%description doc
Jakarta Commons Modeller documentation.

%description doc -l pl.UTF-8
Dokumentacja do Jakarta Commons Modeller.

%prep
%setup -q -n commons-modeler-%{version}-src

%build
cat << EOF > build.properties
commons-digester.jar=%{_javadir}/commons-digester.jar
commons-logging.jar=%{_javadir}/commons-logging.jar
jmx.jar=%{_javadir}/jmxri.jar
jmxtools.jar=%{_javadir}/jmxtools.jar
EOF
ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install dist/*.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt PROPOSAL.html RELEASE-NOTES* STATUS.html
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs
