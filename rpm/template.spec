Name:           ros-indigo-rqt-gui-py
Version:        0.2.14
Release:        1%{?dist}
Summary:        ROS rqt_gui_py package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_gui_py
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-qt-gui >= 0.2.17
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rqt-gui
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-qt-gui
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rqt-gui

%description
rqt_gui_py enables GUI plugins to use the Python client library for ROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.14-1
- Autogenerated by Bloom

