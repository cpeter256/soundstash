from django.shortcuts import render
from django.http import HttpResponse
import json

json_data = '[{"title":"0ozdignzo5bp6do1b22b792a","url":"whzzmw3fvwvobu"},{"title":"3_mtu5kq0cx0","url":"t8iaqwbxse6b7"},{"title":"3vdpqp3x1k","url":"6ryo2y93d00"},{"title":"9ci7pqt8mon__5jp","url":"hnngkoe3ob1g.h"},{"title":"sn4jyrkgzwg3v","url":"o7cjf7o0cva9i6zwhrzqsrpm"},{"title":"zosje0cfxxtd","url":"4vowbp4z_oi36s_cdts"},{"title":".mraljsmrxobs.","url":"elp.v.rv48"},{"title":"tr_.1lla31h","url":"xrtlhjlkv0_0cg3oour"},{"title":"qcxjr.s3","url":"2wk5icvs_le077hp"},{"title":"d_r3bd","url":"rwoi.qbilgg41"},{"title":"2bltp0j.jcf","url":"ch9ah"},{"title":"kbbw984","url":"jieyyi"},{"title":"sgpr4n.yru1wlk05c","url":"t15x2z2s0"},{"title":"ze17osv943g","url":"u98ry102y36qkwrjfla5qo"},{"title":"7zlvnj34vh3","url":"cp0elg3mar"},{"title":"l73f378w3hqonev8","url":"y6obbf.jwz4"},{"title":"x_0rflwxmfl.s","url":"nb4qkgrrtn49w82dddfjkx"},{"title":"uz2n79xil6j30.1m0xf","url":"helap7elksr9ybn9fl"},{"title":"55wt9udh9qaczq","url":"gixscc.7qkf1kgtn_omp0y"},{"title":"l2i7gbfa53u","url":"mxowf"}]'

data = json.loads(json_data)

def libraryView(request):
	return HttpResponse(json.dumps(data), content_type='application/json')

# Create your views here.
