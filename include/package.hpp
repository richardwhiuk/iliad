#ifndef ILIAD_FILE_PACKAGE
#define ILIAD_FILE_PACKAGE

#include <module.hpp>

namespace Iliad {

class Package {

public:
	Package(Server& server);
	virtual ~Package();

	std::map<std::string, Module> modules();

};

}

#endif
