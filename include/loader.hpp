#include <iliad.hpp>
#include <package.hpp>

namespace Iliad {

class Loader {

public:

	Loader(Server& server);
	virtual ~Loader();

	virtual std::map<std::string, Package> packages() = 0;


};

}
