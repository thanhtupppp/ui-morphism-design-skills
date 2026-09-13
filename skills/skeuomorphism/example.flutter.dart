import 'package:flutter/material.dart';

class SkeuomorphicControl extends StatelessWidget {
  const SkeuomorphicControl({super.key});

  @override
  Widget build(BuildContext context) {
    return DecoratedBox(
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
          colors: [Color(0xFFD9D4C7), Color(0xFFAAA397)],
        ),
        border: Border.all(color: const Color(0xFF756F66)),
        borderRadius: BorderRadius.circular(10),
        boxShadow: const [
          BoxShadow(color: Color(0x47000000), offset: Offset(0, 4), blurRadius: 8),
        ],
      ),
      child: Semantics(
        button: true,
        label: 'Skeuomorphic control',
        child: Padding(
          padding: const EdgeInsets.all(12),
          child: FilledButton(onPressed: () {}, child: const Text('Activate')),
        ),
      ),
    );
  }
}
