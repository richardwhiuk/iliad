#include <iostream>
#include <string>

#include <log.hpp>

namespace Iliad {

namespace CGI {

class Log : public Iliad::Log {

public:
	Log(std::ostream& out);

	virtual void operator()(Iliad::Exception& e){
		log << e.what() << std::endl;
	}

	virtual ~Log();

private:
	std::ostream& log;

};

}

}

