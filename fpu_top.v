// Authors: Hunter Frederick, Ben Updike, Sean Cordrey, Nicholas Longest

module fpu_top(CLOCK_50, KEY);

	input       CLOCK_50; 
	input [3:0]      KEY;
   
	wire [63:0] opA, opB;
	wire  [1:0] rmode;
	wire  [2:0] fpu_op;
	wire        key0out;
	
	wire [11:0] addrPoint;
	
	wire[69:0] outs1, outs2, outs3, outs4, outs5, outs6, outs7, outs8;
	
	wire[71:0] memOuts1, memOuts2, memOuts3, memOuts4, memOuts5, memOuts6, memOuts7, memOuts8;
	
	wire		  ready1;
	
	wire pllCLK;
   
   PLL60 pll(
      .refclk(CLOCK_50),
		.rst(),
		.outclk_0(pllCLK)
      );
	
	// Only used for testing purposes
	keypress key0(pllCLK, 1'b1, KEY[0], key0out);
	
 
	// ROM holding operand A values for FPU
	rom_64x256 aIn(addrPoint, pllCLK, opA);
	
	// ROM holding operand B values for FPU
	romOpB bIn(addrPoint, pllCLK, opB);
	
	// ROM holding rmode value for FPU
	rom_rmode rIn(addrPoint, pllCLK, rmode);
	
	// ROM holding opcode value for FPU
	rom_fpuOP fpuIn(addrPoint, pllCLK, fpu_op);
	
	count addrCycler(pllCLK, ready1, addrPoint);
	 
	ram_t mem1
	(
		.address(addrPoint),
		.clock(pllCLK),
		.data(outs1),
		.wren(ready1),
		.q(memOuts1)
	);
	
	ram_t mem2
	(
		.address(addrPoint),
		.clock(pllCLK),
		.data(outs2),
		.wren(ready1),
		.q(memOuts2)
	);
	
	ram_t mem3
	(
		.address(addrPoint),
		.clock(pllCLK),
		.data(outs3),
		.wren(ready1),
		.q(memOuts3)
	);
	
	ram_t mem4
	(
		.address(addrPoint),
		.clock(pllCLK),
		.data(outs4),
		.wren(ready1),
		.q(memOuts4)
	);
	
	ram_t mem5
	(
		.address(addrPoint),
		.clock(pllCLK),
		.data(outs5),
		.wren(ready1),
		.q(memOuts5)
	);
	
	ram_t mem6
	(
		.address(addrPoint),
		.clock(pllCLK),
		.data(outs6),
		.wren(ready1),
		.q(memOuts6)
	);
	
	ram_t mem7
	(
		.address(addrPoint),
		.clock(pllCLK),
		.data(outs7),
		.wren(ready1),
		.q(memOuts7)
	);
	
	ram_t mem8
	(
		.address(addrPoint),
		.clock(pllCLK),
		.data(outs8),
		.wren(ready1),
		.q(memOuts8)
	);
	
   fpu	 fpu1( pllCLK, key0out, ready1, rmode, fpu_op, opA, opB, outs1[69:6], outs1[5], 
	          outs1[4], outs1[3], outs1[2], outs1[1], outs1[0]);
				 
	fpu	 fpu2( pllCLK, key0out, ready1, rmode, fpu_op, opA, opB, outs2[69:6], outs2[5], 
	          outs2[4], outs2[3], outs2[2], outs2[1], outs2[0]);
	
	fpu	 fpu3( pllCLK, key0out, ready1, rmode, fpu_op, opA, opB, outs3[69:6], outs3[5], 
	          outs3[4], outs3[3], outs3[2], outs3[1], outs3[0]);
	
	fpu	 fpu4( pllCLK, key0out, ready1, rmode, fpu_op, opA, opB, outs4[69:6], outs4[5], 
	          outs4[4], outs4[3], outs4[2], outs4[1], outs4[0]);
				 
	fpu	 fpu5( pllCLK, key0out, ready1, rmode, fpu_op, opA, opB, outs5[69:6], outs5[5], 
	          outs5[4], outs5[3], outs5[2], outs5[1], outs5[0]);
				 
	fpu	 fpu6( pllCLK, key0out, ready1, rmode, fpu_op, opA, opB, outs6[69:6], outs6[5], 
	          outs6[4], outs6[3], outs6[2], outs6[1], outs6[0]);
				 
	fpu	 fpu7( pllCLK, key0out, ready1, rmode, fpu_op, opA, opB, outs7[69:6], outs7[5], 
	          outs7[4], outs7[3], outs7[2], outs7[1], outs7[0]);
				 
	fpu	 fpu8( pllCLK, key0out, ready1, rmode, fpu_op, opA, opB, outs8[69:6], outs8[5], 
	          outs8[4], outs8[3], outs8[2], outs8[1], outs8[0]);
				 

	pulseGen readyPulse1(.clk(pllCLK), .in(outs1[5]), .out(ready1));
	
endmodule

module pulseGen(
	input wire clk, in,
	output reg out);
	reg in_old;
	
	always @(posedge clk) begin
			in_old <= in;
			out = ~in_old && in;
	end
endmodule
