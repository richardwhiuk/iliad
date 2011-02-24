
#include <iliad.hpp>
#include <package.hpp>

#include <string>

namespace Iliad {

namespace Core {

namespace Config {

class Package : public Iliad::Package {

public:

	Package(Iliad::Server& server);
	virtual ~Package();
	
	virtual std::string name();

	virtual std::map<std::string, Iliad::Module*> modules();

};

}

}

}
