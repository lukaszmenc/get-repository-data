# GetRepository

GetRepository is a small backend REST service allowing the user to view the most important details about the selected 
GitHub repository.

## Installation

Rename `.env.example` to `.env` and fill it with your [GitHub personal access token](https://github.com/settings/tokens).

## Usage

### Development

Service can be easily run locally using docker-compose `docker-compose up`.

The service will be available at [http://localhost:5000](http://localhost:5000)

### Production

Build image using `docker build -t getrepo_api .`

Run API using `docker run -d -p 5000:5000 getrepo_api`

The service will be available at [http://localhost:5000](http://localhost:5000)

## API endpoints

| Endpoint                     | Method | Result             |
| ---------------------------- | ------ | ------------------ |
| `/repositories/:owner/:repo` | GET    | Repository details |

## Tests

To run tests, simply run `pytest`.

Note: Before running tests, install required packages using `pip install -r requirements`.

## Performance tests

Performed with ApacheBench v2.3.

```
Server Software:        Werkzeug/0.16.0
Server Hostname:        localhost
Server Port:            5000

Document Path:          /repositories/lukaszmenc/locapi
Document Length:        189 bytes

Concurrency Level:      20
Time taken for tests:   3.663 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      336000 bytes
HTML transferred:       189000 bytes
Requests per second:    272.99 [#/sec] (mean)
Time per request:       73.263 [ms] (mean)
Time per request:       3.663 [ms] (mean, across all concurrent requests)
Transfer rate:          89.57 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.4      0       5
Processing:    24   64  13.6     64     428
Waiting:        5   61  13.4     60     423
Total:         27   65  13.5     64     428

Percentage of the requests served within a certain time (ms)
  50%     64
  66%     66
  75%     68
  80%     70
  90%     74
  95%     77
  98%     80
  99%     82
 100%    428 (longest request)
```
