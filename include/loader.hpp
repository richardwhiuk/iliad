#ifndef ILIAD_FILE_LOADER
#define ILIAD_FILE_LOADER

#include <string>

#include <iliad.hpp>
#include <package.hpp>

namespace Iliad {

class Loader {

public:

	Loader(Iliad::Server& server);
	virtual ~Loader();

	virtual std::map<std::string, Iliad::Package*> packages() = 0;

	virtual std::string name() = 0;

};

}

#endif

