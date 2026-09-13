import 'package:flutter/material.dart';

class NeoButton extends StatelessWidget {
  const NeoButton({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: const Color(0xFFFFDC58),
        border: Border.all(color: Colors.black, width: 2),
        boxShadow: const [BoxShadow(color: Colors.black, offset: Offset(4, 4))],
      ),
      child: FilledButton(
        style: FilledButton.styleFrom(
          backgroundColor: const Color(0xFFFFDC58),
          foregroundColor: Colors.black,
          elevation: 0,
          shape: const RoundedRectangleBorder(borderRadius: BorderRadius.zero),
        ),
        onPressed: () {},
        child: const Text('Publish'),
      ),
    );
  }
}
