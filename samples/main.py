# Copyright (c) 2023 Innodisk Corporation
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


from .intel_sample import init_intel_samples
from .xlnx_sample import init_xlnx_samples
from .hailo_sample import init_hailo_samples
from .nvidia_sample import init_nvidia_samples


def init_samples(framework: str):
    """ Initialize Samples into Database """

    sample_table = {
        'openvino': init_intel_samples,
        'vitis-ai': init_xlnx_samples,
        'hailort': init_hailo_samples,
        'tensorrt': init_nvidia_samples
    }
    func = sample_table.get(framework.strip().lower(), None) 
    
    if func is None: 
        raise RuntimeError('Unexpected framework: {}'.format(framework))

    func()
