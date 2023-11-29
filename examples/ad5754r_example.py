# Copyright (C) 2023 Analog Devices, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#     - Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     - Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#     - Neither the name of Analog Devices, Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#     - The use of this software may or may not infringe the patent rights
#       of one or more patent holders.  This license does not release you
#       from the requirement that you obtain separate licenses from these
#       patent holders to use this software.
#     - Use of the software either in source or binary form, must be run
#       on or directly connected to an Analog Devices Inc. component.
#
# THIS SOFTWARE IS PROVIDED BY ANALOG DEVICES "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED.
#
# IN NO EVENT SHALL ANALOG DEVICES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, INTELLECTUAL PROPERTY
# RIGHTS, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from adi.ad5754r import *

# Set up AD5754R
ad5754r_dev = ad5754r(uri="serial:COM4,230400,8n1n")
ad5754r_dev.int_ref_powerup = "powerup"

# Configure channel 0
chn_num = 0
ad5754r_chan = ad5754r_dev.channel[chn_num]
ad5754r_chan.powerup = "powerup"

# Update dac output for channel 0 instantaneously using the 'raw' attribute
ad5754r_chan.raw = 1600

# Update dac output for channel 0 using software LDAC operation
ad5754r_chan.dac_register = 500
ad5754r_dev.sw_ldac_trigger = "Trigger"

# Update dac output of channel 0 using hardware LDAC operation
ad5754r_chan.dac_register = 1000
ad5754r_dev.hw_ldac_trigger = "Trigger"

# Clear all DAC outputs to the midscale code
ad5754r_dev.clear_setting = "midscale_code"
ad5754r_dev.all_chns_clear = "Clear"

# Determine output voltage using scale and offset
raw = int(ad5754r_chan.raw)
scale = float(ad5754r_chan.scale)
offset = int(ad5754r_chan.offset)
print(f"Channel{chn_num} voltage: {(raw + offset) * scale}")
