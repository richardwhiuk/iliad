#include <request.hpp>
#include <response.hpp>

namespace Iliad {

class Server {

public:
	virtual ~Server();

	virtual void process(Iliad::Request& req, Iliad::Response& rep);

protected:
	Server();

};

}

