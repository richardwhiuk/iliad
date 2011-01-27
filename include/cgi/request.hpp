#include <iostream>
#include <vector>
#include <string>

#include <request.hpp>

namespace Iliad {
namespace CGI {

class Request : public Iliad::Request {

public:

	Request(int argc, char** argv, std::istream& in);

	Request(std::vector<std::string>& args, std::istream& in);

};

}
}

